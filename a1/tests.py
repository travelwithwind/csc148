import course
import survey
import criterion
import grouper
import pytest

from a1.course import Student, Course
from a1.criterion import HomogeneousCriterion, HeterogeneousCriterion
from a1.grouper import slice_list
from a1.survey import Question, Answer, MultipleChoiceQuestion, Survey, \
    NumericQuestion, YesNoQuestion, CheckboxQuestion


class TestStudent:

    def test_has_answer(self) -> None:
        student1 = Student(1, "Mario")
        question1 = Question(1, "Question1")
        answer1 = Answer("Answer1")
        assert not student1.has_answer(question1)

    def test_set_answer(self) -> None:
        student1 = Student(1, "Mario")
        question1 = Question(1, "Question1")
        answer1 = Answer("Answer1")
        assert not student1.has_answer(question1)

    def test_get_answer(self) -> None:
        student1 = Student(1, "Mario")
        question1 = Question(1, "Question1")
        answer1 = Answer("Answer1")
        assert student1.get_answer(question1) is None


class TestCourse:


    def test_enroll_students(self) -> None:
        # successfully enrolled
        course1 = Course("CSC148")
        student1 = Student(1, "Mario")
        multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        survey1 = Survey([multi1])
        course1.enroll_students([student1])
        assert len(course1.students) == 1

    def test_all_answered(self) -> None:
        # return true if empty
        course1 = Course("CSC148")
        student1 = Student(1, "Mario")
        multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        survey1 = Survey([multi1])
        assert course1.all_answered(survey1)

    def test_get_students(self) -> None:
        # empty at first
        course1 = Course("CSC148")
        student1 = Student(1, "Mario")
        multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        survey1 = Survey([multi1])
        assert course1.get_students() == ()


class TestMultipleChoiceQuestion:
    def test_validate_answer(self) -> None:
        # content is Multiple Choice
        multi1 = MultipleChoiceQuestion\
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        answer1 = Answer("A")
        assert multi1.validate_answer(answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        answer1 = Answer("A")
        answer2 = Answer("A")
        assert self.get_similarity(answer1.content, answer2.content) \
               == 1.0


class TestNumericQuestion:

    def test_validate_answer(self) -> None:
        # content is Numeric
        numeric1 = NumericQuestion(1, "Numeric1", 0, 5)
        answer1 = Answer(1)
        answer2 = Answer(1)
        assert numeric1.validate_answer(answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        numeric1 = NumericQuestion(1, "Numeric1", 0, 5)
        answer1 = Answer(1)
        answer2 = Answer(1)
        assert self.get_similarity(self.answer1.content, self.answer2.content) \
               == 1.0


class TestYesNoQuestionQuestion:

    def test_validate_answer(self) -> None:
        # content is Yesno Question
        yesno1 = YesNoQuestion(1, "YesNo1")
        answer1 = Answer(True)
        answer2 = Answer(True)
        assert yesno1.validate_answer(answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        yesno1 = YesNoQuestion(1, "YesNo1")
        answer1 = Answer(True)
        answer2 = Answer(True)
        assert self.get_similarity(answer1.content, answer2.content) \
               == 1.0


class TestCheckboxQuestion:

    def test_validate_answer(self) -> None:
        # content is not checkbox Question
        checkbox1 = CheckboxQuestion(1, "Checkbox", ["A", "B", "C", "D"])
        answer1 = Answer("A")
        answer2 = Answer("A")
        assert checkbox1.validate_answer(answer1) == False

    def test_get_similarity(self) -> None:
        # content the same, return 1
        checkbox1 = CheckboxQuestion(1, "Checkbox", ["A", "B", "C", "D"])
        answer1 = Answer("A")
        answer2 = Answer("A")
        assert self.get_similarity(answer1.content, answer2.content) \
               == 1.0


class TestAnswer:

    def test_is_valid(self) -> None:
        # content is Multiple Choice
        multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        answer1 = Answer("A")
        answer2 = Answer("A")
        assert multi1.validate_answer(answer1)


class TestHomogeneousCriterion:

    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        choices = "A"
        c = criterion.HomogeneousCriterion()
        question1 = MultipleChoiceQuestion(1, "Multi1", "A")

        assert c.score_answers(question1, [Answer(choices)]) \
               == 1


class TestHeterogeneousCriterion:

    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        choices = "A"
        c = criterion.HeterogeneousCriterion()
        question1 = MultipleChoiceQuestion(1, "Multi1", "A")
        assert c.score_answers(question1, [Answer(choices)]) \
               == 0


class LonelyMemberCriterion:
    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        choices = "A"
        c = criterion.LonelyMemberCriterion()
        question1 = MultipleChoiceQuestion(1, "Multi1", "A")
        assert self.c.score_answers(self.question11, [Answer(self.choices)]) \
               == 0


class TestGroup:

    def test_get_members(self) -> None:
        # no member can get
        group = grouper.Group([])
        assert len(group.get_members()) == 0


class TestGrouping:

    def test_add_group(self) -> None:
        group = grouper.Grouping()
        assert group.add_group(grouper.Group([])) == False

    def test_get_groups(self) -> None:
        student = [course.Student(i, "148" + str(i)) for i in range(10)]
        group = grouper.Grouping()
        group.add_group(grouper.Group([student[1]]))
        assert len(group.get_groups()) == 1



class TestSurvey:
    def test_get_questions(self) -> None:
        student = course.Student(1, "CSC148")
        question = survey.YesNoQuestion(1, "YesNo")
        student.set_answer(question, survey.Answer(True))
        sur = survey.Survey([])
        assert sur.get_questions() == []

    def test_get_criterion(self) -> None:
        student = course.Student(1, "CSC148")
        question = survey.YesNoQuestion(1, "YesNo")
        student.set_answer(question, survey.Answer(True))
        sur = survey.Survey([])



    def test_get_weight(self) -> None:
        student = course.Student(1, "CSC148")
        question = survey.YesNoQuestion(1, "YesNo")
        student.set_answer(question, survey.Answer(True))
        sur = survey.Survey([question])
        sur.set_weight(5, question)
        assert question.get_weight() == 5

    def test_score_student(self) -> None:
        student = course.Student(1, "CSC148")
        question = survey.YesNoQuestion(1, "YesNo")
        student.set_answer(question, survey.Answer(True))
        sur = survey.Survey([question])
        sur.set_weight(5, question)
        assert sur.score_students([student]) == 5.0

    def test_score_grouping(self) -> None:
        sur = survey.Survey([])
        assert sur.score_grouping(grouper.Grouping()) == 0



def test_slice_list(self) -> None:
    assert slice_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def windows(self) -> None:
    assert windows([1, 2, 3], 2) == [[1, 2], [2, 3]]


class TestAlphaGrouper:
    def test_make_grouping(self) -> None:
        course1 = Course("CSC148")
        student = [course.Student(i, "148" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "1" + str(i), 1, 10) for i in range(5)]
        sur = survey.Survey(questions)
        course1.enroll_students(student)
        group1 = grouper.AlphaGrouper(1).make_grouping(course1, sur)
        assert len(group1) == 5

class TestRandomGrouper:
    def test_make_grouping(self) -> None:
        course1 = Course("CSC148")
        student = [course.Student(i, "148" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "1" + str(i), 1, 10) for i in range(5)]
        sur = survey.Survey(questions)
        course1.enroll_students(student)
        group1 = grouper.RandomGrouper(1).make_grouping(course1, sur)
        assert len(group1) == 5

class TestGreedyGrouper:
    def test_make_grouping(self) -> None:
        course1 = Course("CSC148")
        student = [course.Student(i, "148" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "1" + str(i), 1, 10) for i in range(5)]
        sur = survey.Survey(questions)
        course1.enroll_students(student)
        group1 = grouper.GreedyGrouper(1).make_grouping(course1, sur)
        assert len(group1) == 5

class TestWindowGrouper:
    def test_make_grouping(self) -> None:
        course1 = Course("CSC148")
        student = [course.Student(i, "148" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "1" + str(i), 1, 10) for i in range(5)]
        sur = survey.Survey(questions)
        course1.enroll_students(student)
        group1 = grouper.WindowGrouper(1).make_grouping(course1, sur)
        assert len(group1) == 5



if __name__ == '__main__':

    pytest.main(['tests.py'])
