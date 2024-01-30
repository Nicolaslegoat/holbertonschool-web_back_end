/* eslint-disable */
export default function updateStudentGradeByCity(students, city,newGrades) {
    return students.filter((student) => student.location === city)
    .map((student) => {
        const found_grade = newGrades.find((grade) => grade.studentId === studentId);
        if (found_grade) {
            return { ...student, grade: found_grade.grade };
        }
        return { ...student, grade: 'N/A' };
    });
}