"""
🎓 Student Management System - Modern Streamlit Web Application
Features:
- Live Interactive Dashboard with Key Performance Metrics
- Student Directory with Search, Sort, Filter, and CSV Export
- Add New Student with Validation
- Edit Student Details & Subject Marks
- Student Visual Report Card
- Analytics with Plotly Charts (Subject Averages, Grade Distribution, Leaderboard)
- Safe File Synchronization with students.txt
"""

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configure Page
st.set_page_config(
    page_title="Student Management Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #64748B;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .report-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .badge-pass {
        background-color: #10B981;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-fail {
        background-color: #EF4444;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-pending {
        background-color: #F59E0B;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")


class Student:
    """Represents a student record with academic evaluation methods."""

    def __init__(self, student_id, name, maths=None, physics=None, chemistry=None):
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def has_marks(self):
        return (
            self.maths is not None
            and self.physics is not None
            and self.chemistry is not None
        )

    def total_marks(self):
        if self.has_marks():
            return self.maths + self.physics + self.chemistry
        return None

    def percentage(self):
        total = self.total_marks()
        if total is not None:
            return round(total / 3.0, 2)
        return None

    def grade(self):
        pct = self.percentage()
        if pct is None:
            return "N/A"
        if pct >= 90:
            return "A+"
        if pct >= 80:
            return "A"
        if pct >= 70:
            return "B"
        if pct >= 60:
            return "C"
        if pct >= 50:
            return "D"
        return "F"

    def status(self):
        if not self.has_marks():
            return "Pending"
        if self.maths >= 33 and self.physics >= 33 and self.chemistry >= 33:
            return "Pass"
        return "Fail"


def load_students():
    """Load students dict from students.txt."""
    students = {}
    if not os.path.exists(DATA_FILE):
        return students

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 5:
                    continue
                sid, sname, m, p, c = parts
                try:
                    m_val = None if m == "None" else int(m)
                    p_val = None if p == "None" else int(p)
                    c_val = None if c == "None" else int(c)
                except ValueError:
                    continue
                students[sid] = Student(sid, sname, m_val, p_val, c_val)
    except Exception as e:
        st.error(f"Error loading student database: {e}")
    return students


def save_students(students):
    """Save students dict to students.txt."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for sid, s in students.items():
                f.write(f"{sid}:{s.name}:{s.maths}:{s.physics}:{s.chemistry}\n")
        return True
    except Exception as e:
        st.error(f"Error saving to database: {e}")
        return False


def get_students_dataframe(students):
    """Convert students dictionary to pandas DataFrame."""
    rows = []
    for sid, s in students.items():
        total = s.total_marks()
        pct = s.percentage()
        rows.append(
            {
                "ID": sid,
                "Name": s.name,
                "Maths": s.maths if s.maths is not None else None,
                "Physics": s.physics if s.physics is not None else None,
                "Chemistry": s.chemistry if s.chemistry is not None else None,
                "Total (300)": total,
                "Percentage (%)": pct,
                "Grade": s.grade(),
                "Status": s.status(),
            }
        )
    df = pd.DataFrame(rows)
    if not df.empty:
        df["Numeric_ID"] = pd.to_numeric(df["ID"], errors="coerce")
        df = df.sort_values(by="Numeric_ID", ascending=True).drop(
            columns=["Numeric_ID"]
        )
    return df


# Main State Initialization
if "students" not in st.session_state:
    st.session_state.students = load_students()

students = st.session_state.students
df = get_students_dataframe(students)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 🎓 Navigation")
    menu = st.radio(
        "Go to page:",
        [
            "📊 Dashboard & Overview",
            "📋 Student Directory",
            "➕ Add New Student",
            "✏️ Update Student / Marks",
            "🔍 Search & Report Card",
            "📈 Class Analytics & Charts",
            "🗑️ Delete Student",
        ],
        index=0,
    )
    st.markdown("---")
    st.markdown(
        f"**Database Status:**\n- 📁 File: `{os.path.basename(DATA_FILE)}`\n- 👥 Records: **{len(students)}**"
    )
    if st.button("🔄 Reload from File", use_container_width=True):
        st.session_state.students = load_students()
        st.rerun()

# ----------------- PAGE 1: DASHBOARD & OVERVIEW -----------------
if menu == "📊 Dashboard & Overview":
    st.markdown(
        '<div class="main-header">🎓 Student Management Portal</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Overview of class academic performance and quick student records</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    total_count = len(students)
    evaluated_students = [s for s in students.values() if s.has_marks()]
    eval_count = len(evaluated_students)

    with col1:
        st.metric(label="👥 Total Enrolled", value=total_count)

    with col2:
        st.metric(
            label="📝 Evaluated Records",
            value=f"{eval_count} / {total_count}",
            delta=f"{round((eval_count/total_count)*100, 1)}%"
            if total_count > 0
            else None,
        )

    if evaluated_students:
        avg_pct = round(
            sum(s.percentage() for s in evaluated_students) / eval_count, 2
        )
        passed = sum(1 for s in evaluated_students if s.status() == "Pass")
        pass_rate = round((passed / eval_count) * 100, 1)
        topper = max(evaluated_students, key=lambda s: s.total_marks())
    else:
        avg_pct = 0.0
        pass_rate = 0.0
        topper = None

    with col3:
        st.metric(label="📊 Class Average", value=f"{avg_pct}%")

    with col4:
        st.metric(label="🎯 Pass Rate", value=f"{pass_rate}%")

    st.markdown("---")

    # Topper Spotlight Banner
    if topper:
        st.success(
            f"🏆 **Class Topper Spotlight:** **{topper.name}** (ID: `{topper.student_id}`) — Score: **{topper.total_marks()} / 300** ({topper.percentage()}%) with Grade **{topper.grade()}**!"
        )

    # Quick Summary Table
    st.subheader("📋 Quick Student Roster")
    if not df.empty:
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "Percentage (%)": st.column_config.ProgressColumn(
                    "Percentage (%)",
                    format="%.2f%%",
                    min_value=0,
                    max_value=100,
                ),
                "Status": st.column_config.TextColumn("Status"),
            },
            hide_index=True,
        )
    else:
        st.info("No students added yet! Use the 'Add New Student' tab.")


# ----------------- PAGE 2: STUDENT DIRECTORY -----------------
elif menu == "📋 Student Directory":
    st.markdown(
        '<div class="main-header">📋 Student Directory</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Browse, search, filter, and export the student database</div>',
        unsafe_allow_html=True,
    )

    if df.empty:
        st.info("No student records available.")
    else:
        # Filters Row
        f_col1, f_col2, f_col3 = st.columns([2, 1, 1])
        with f_col1:
            search_text = st.text_input(
                "🔍 Search by ID or Name:", placeholder="Type to filter..."
            )
        with f_col2:
            status_filter = st.selectbox(
                "Filter by Result:", ["All", "Pass", "Fail", "Pending"]
            )
        with f_col3:
            grade_filter = st.selectbox(
                "Filter by Grade:", ["All", "A+", "A", "B", "C", "D", "F", "N/A"]
            )

        filtered_df = df.copy()
        if search_text:
            filtered_df = filtered_df[
                filtered_df["ID"]
                .astype(str)
                .str.contains(search_text, case=False, na=False)
                | filtered_df["Name"].str.contains(
                    search_text, case=False, na=False
                )
            ]
        if status_filter != "All":
            filtered_df = filtered_df[filtered_df["Status"] == status_filter]
        if grade_filter != "All":
            filtered_df = filtered_df[filtered_df["Grade"] == grade_filter]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            column_config={
                "Percentage (%)": st.column_config.ProgressColumn(
                    "Percentage (%)", format="%.2f%%", min_value=0, max_value=100
                ),
            },
            hide_index=True,
        )

        st.caption(f"Showing {len(filtered_df)} of {len(df)} student(s)")

        # Export CSV Button
        csv_data = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Export Table as CSV",
            data=csv_data,
            file_name="students_records.csv",
            mime="text/csv",
            use_container_width=False,
        )


# ----------------- PAGE 3: ADD NEW STUDENT -----------------
elif menu == "➕ Add New Student":
    st.markdown(
        '<div class="main-header">➕ Add New Student</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Enroll a new student and optionally record their initial marks</div>',
        unsafe_allow_html=True,
    )

    with st.form("add_student_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            new_id = st.text_input(
                "Student ID *",
                placeholder="e.g. 103",
                help="Unique numeric identification number",
            )
        with col2:
            new_name = st.text_input(
                "Student Full Name *",
                placeholder="e.g. Rohan Gupta",
                help="Letters and spaces only",
            )

        st.markdown("#### Subject Marks (Optional - can be updated later)")
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            enter_maths = st.number_input(
                "Maths Marks (0-100)",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Leave blank to skip",
            )
        with m_col2:
            enter_physics = st.number_input(
                "Physics Marks (0-100)",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Leave blank to skip",
            )
        with m_col3:
            enter_chem = st.number_input(
                "Chemistry Marks (0-100)",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Leave blank to skip",
            )

        submitted = st.form_submit_button(
            "✨ Add Student", use_container_width=True
        )

        if submitted:
            new_id = new_id.strip()
            new_name = new_name.strip()

            if not new_id:
                st.error("Student ID cannot be empty!")
            elif not new_id.isdigit():
                st.error("Student ID must be a numeric value!")
            elif new_id in students:
                st.error(f"Student ID '{new_id}' already exists!")
            elif not new_name:
                st.error("Student name cannot be empty!")
            elif not new_name.replace(" ", "").isalpha():
                st.error("Student name should only contain letters and spaces!")
            else:
                s = Student(
                    student_id=new_id,
                    name=new_name,
                    maths=enter_maths,
                    physics=enter_physics,
                    chemistry=enter_chem,
                )
                students[new_id] = s
                if save_students(students):
                    st.success(
                        f"Student **{new_name}** (ID: `{new_id}`) successfully registered!"
                    )
                    st.session_state.students = students
                    st.rerun()


# ----------------- PAGE 4: UPDATE STUDENT / MARKS -----------------
elif menu == "✏️ Update Student / Marks":
    st.markdown(
        '<div class="main-header">✏️ Update Student Records</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Modify student names or record and update subject scores</div>',
        unsafe_allow_html=True,
    )

    if not students:
        st.info("No students available to update.")
    else:
        student_options = {
            f"{sid} - {s.name}": sid for sid, s in students.items()
        }
        selected_label = st.selectbox(
            "Select Student to Edit:", list(student_options.keys())
        )
        selected_id = student_options[selected_label]
        target_student = students[selected_id]

        with st.form("update_form"):
            st.markdown(f"### Editing ID: `{selected_id}`")
            updated_name = st.text_input("Full Name:", value=target_student.name)

            col1, col2, col3 = st.columns(3)
            with col1:
                cur_maths = (
                    target_student.maths
                    if target_student.maths is not None
                    else 0
                )
                maths_val = st.number_input(
                    "Maths (0-100):",
                    min_value=0,
                    max_value=100,
                    value=cur_maths,
                )
            with col2:
                cur_phys = (
                    target_student.physics
                    if target_student.physics is not None
                    else 0
                )
                phys_val = st.number_input(
                    "Physics (0-100):",
                    min_value=0,
                    max_value=100,
                    value=cur_phys,
                )
            with col3:
                cur_chem = (
                    target_student.chemistry
                    if target_student.chemistry is not None
                    else 0
                )
                chem_val = st.number_input(
                    "Chemistry (0-100):",
                    min_value=0,
                    max_value=100,
                    value=cur_chem,
                )

            update_btn = st.form_submit_button(
                "💾 Save Changes", use_container_width=True
            )

            if update_btn:
                updated_name = updated_name.strip()
                if not updated_name:
                    st.error("Name cannot be empty!")
                elif not updated_name.replace(" ", "").isalpha():
                    st.error("Name must contain letters and spaces only!")
                else:
                    target_student.name = updated_name
                    target_student.maths = maths_val
                    target_student.physics = phys_val
                    target_student.chemistry = chem_val
                    if save_students(students):
                        st.success(
                            f"Student record for **{updated_name}** updated successfully!"
                        )
                        st.session_state.students = students
                        st.rerun()


# ----------------- PAGE 5: SEARCH & REPORT CARD -----------------
elif menu == "🔍 Search & Report Card":
    st.markdown(
        '<div class="main-header">🔍 Student Academic Report Card</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Search a student and view their official digital report card</div>',
        unsafe_allow_html=True,
    )

    query = st.text_input(
        "Enter Student ID or Full/Partial Name:",
        placeholder="e.g. 101 or Priya",
    )

    if query:
        matches = [
            s
            for s in students.values()
            if query.lower() in s.student_id.lower()
            or query.lower() in s.name.lower()
        ]

        if not matches:
            st.warning(f"No student record found matching '{query}'.")
        else:
            for s in matches:
                st.markdown("---")
                # Report Card UI
                with st.container():
                    col_info, col_metrics = st.columns([1, 1])
                    with col_info:
                        st.markdown(f"### 👤 {s.name}")
                        st.markdown(f"**Student ID:** `{s.student_id}`")
                        status_class = (
                            "badge-pass"
                            if s.status() == "Pass"
                            else (
                                "badge-fail"
                                if s.status() == "Fail"
                                else "badge-pending"
                            )
                        )
                        st.markdown(
                            f"**Status:** <span class='{status_class}'>{s.status().upper()}</span>",
                            unsafe_allow_html=True,
                        )

                    with col_metrics:
                        c1, c2, c3 = st.columns(3)
                        total_score = s.total_marks()
                        pct = s.percentage()
                        c1.metric(
                            "Total",
                            f"{total_score}/300"
                            if total_score is not None
                            else "N/A",
                        )
                        c2.metric(
                            "Percentage", f"{pct}%" if pct is not None else "N/A"
                        )
                        c3.metric("Grade", s.grade())

                    # Subject breakdown radar/bar
                    st.markdown("#### Subject Breakdown")
                    b_col1, b_col2, b_col3 = st.columns(3)
                    with b_col1:
                        st.progress(
                            (s.maths or 0) / 100,
                            text=f"Maths: {s.maths if s.maths is not None else 'N/A'}/100",
                        )
                    with b_col2:
                        st.progress(
                            (s.physics or 0) / 100,
                            text=f"Physics: {s.physics if s.physics is not None else 'N/A'}/100",
                        )
                    with b_col3:
                        st.progress(
                            (s.chemistry or 0) / 100,
                            text=f"Chemistry: {s.chemistry if s.chemistry is not None else 'N/A'}/100",
                        )


# ----------------- PAGE 6: CLASS ANALYTICS & CHARTS -----------------
elif menu == "📈 Class Analytics & Charts":
    st.markdown(
        '<div class="main-header">📈 Class Analytics & Visual Insights</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Data visualization and insights across subject performances</div>',
        unsafe_allow_html=True,
    )

    evaluated = [s for s in students.values() if s.has_marks()]

    if not evaluated:
        st.info("No evaluated student marks available to generate charts.")
    else:
        col_c1, col_c2 = st.columns(2)

        # Chart 1: Subject Averages
        with col_c1:
            avg_maths = sum(s.maths for s in evaluated) / len(evaluated)
            avg_phys = sum(s.physics for s in evaluated) / len(evaluated)
            avg_chem = sum(s.chemistry for s in evaluated) / len(evaluated)

            fig_sub = px.bar(
                x=["Maths", "Physics", "Chemistry"],
                y=[avg_maths, avg_phys, avg_chem],
                color=["Maths", "Physics", "Chemistry"],
                labels={"x": "Subject", "y": "Average Score"},
                title="📚 Subject-wise Class Averages",
                color_discrete_sequence=["#3B82F6", "#8B5CF6", "#EC4899"],
            )
            fig_sub.update_layout(yaxis=dict(range=[0, 100]))
            st.plotly_chart(fig_sub, use_container_width=True)

        # Chart 2: Grade Distribution Donut
        with col_c2:
            grades = [s.grade() for s in evaluated]
            grade_df = pd.DataFrame(grades, columns=["Grade"])
            fig_grades = px.pie(
                grade_df,
                names="Grade",
                title="🎯 Class Grade Distribution",
                hole=0.45,
                color_discrete_sequence=px.colors.qualitative.Prism,
            )
            st.plotly_chart(fig_grades, use_container_width=True)

        # Leaderboard Ranking
        st.subheader("🏆 Class Academic Leaderboard")
        ranked = sorted(
            evaluated, key=lambda s: s.total_marks() or 0, reverse=True
        )
        leaderboard_data = [
            {
                "Rank": f"#{idx+1}",
                "ID": s.student_id,
                "Name": s.name,
                "Total Marks": f"{s.total_marks()}/300",
                "Percentage": f"{s.percentage()}%",
                "Grade": s.grade(),
                "Status": s.status(),
            }
            for idx, s in enumerate(ranked)
        ]
        st.dataframe(pd.DataFrame(leaderboard_data), use_container_width=True, hide_index=True)


# ----------------- PAGE 7: DELETE STUDENT -----------------
elif menu == "🗑️ Delete Student":
    st.markdown(
        '<div class="main-header">🗑️ Remove Student Record</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Permanently remove a student from the system with safeguards</div>',
        unsafe_allow_html=True,
    )

    if not students:
        st.info("No students found in the database.")
    else:
        student_options = {
            f"{sid} - {s.name}": sid for sid, s in students.items()
        }
        del_label = st.selectbox(
            "Select Student to Delete:", list(student_options.keys())
        )
        del_id = student_options[del_label]
        target = students[del_id]

        st.warning(
            f"⚠️ You are about to permanently delete **{target.name}** (ID: `{del_id}`) along with all marks."
        )

        confirm_check = st.checkbox("I confirm that I want to delete this student permanently.")

        if st.button("🚨 Delete Student Now", type="primary", disabled=not confirm_check):
            students.pop(del_id)
            if save_students(students):
                st.success(f"Student ID `{del_id}` deleted successfully!")
                st.session_state.students = students
                st.rerun()
