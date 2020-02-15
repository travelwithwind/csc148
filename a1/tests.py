import course
import survey
import criterion
import grouper
import pytest


class TestStudent:
    def __init__(self):
        self.student1 = Student(1, "Mario")
        self.question1 = Question(1, "Question1")
        self.answer1 = Answer("Answer1")

    def test_has_answer(self) -> None:
        assert not self.student1.has_answer(self.question1)

    def set_answer(self) -> None:
        self._ans[self.question1] = self.answer1
        assert not self.student1.has_answer(self.question1)

    def test_get_answer(self) -> None:
        assert self.student1.get_answer(self.question1) is None


class TestCourse:
    def __init__(self):
        self.course1 = Course("CSC148")
        self.student1 = Student(1, "Mario")
        self.multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        self.survey1 = Survey([self.multi1])

    def test_enroll_students(self) -> None:
        # successfully enrolled
        self.course1.enroll_students([self.student1])
        assert len(self.course1) == 1

    def test_all_answered(self) -> None:
        # return true if empty
        assert self.course1.all_answered(self.survey1)

    def test_get_students(self) -> None:
        # empty at first
        assert self.c1.get_students() == ()


class TestMultipleChoiceQuestion:
    def __init__(self):
        self.multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        self.answer1 = Answer("A")
        self.answer2 = Answer("A")

    def test_validate_answer(self) -> None:
        # content is Multiple Choice
        assert self.multi1.validate_answer(self.answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        assert get_similarity(self.answer1.content, self.answer2.content) \
               == 1.0


class TestNumericQuestion:
    def __init__(self):
        self.numeric1 = NumericQuestion(1, "Numeric1", 0, 5)
        self.answer1 = Answer(1)
        self.answer2 = Answer(1)

    def test_validate_answer(self) -> None:
        # content is Numeric
        assert self.numeric1.validate_answer(self.answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        assert get_similarity(self.answer1.content, self.answer2.content) \
               == 1.0


class TestYesNoQuestionQuestion:
    def __init__(self):
        self.yesno1 = YesNoQuestion(1, "YesNo1", [True, False])
        self.answer1 = Answer(True)
        self.answer2 = Answer(True)

    def test_validate_answer(self) -> None:
        # content is Yesorno Question
        assert self.yesno1.validate_answer(self.answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        assert get_similarity(self.answer1.content, self.answer2.content) \
               == 1.0


class TestCheckboxQuestion:
    def __init__(self):
        self.checkbox1 = CheckboxQuestion(1, "Checkbox", ["A", "B", "C", "D"])
        self.answer1 = Answer("A")
        self.answer2 = Answer("A")

    def test_validate_answer(self) -> None:
        # content is checkbox Question
        assert self.checkbox1.validate_answer(self.answer1)

    def test_get_similarity(self) -> None:
        # content the same, return 1
        assert get_similarity(self.answer1.content, self.answer2.content) \
               == 1.0


class TestAnswer:
    def __init__(self):
        self.multi1 = MultipleChoiceQuestion \
            (1, "Multiple Choice Question 1", ["A", "B", "C", "D"])
        self.answer1 = Answer("A")
        self.answer2 = Answer("A")

    def test_validate_answer(self) -> None:
        # content is Multiple Choice
        assert self.multi1.validate_answer(self.answer1)


class TestHomogeneousCriterion:
    def __init__(self):
        self.choices = "A"
        self.c = HomogeneousCriterion()
        self.question1 = MultipleChoiceQuestion(1, "Multi1", "A")

    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        assert self.c.score_answers(self.question11, [Answer(self.choices)]) \
               == 1


class TestHeterogeneousCriterion:
    def __init__(self):
        self.choices = "A"
        self.c = HeterogeneousCriterion()
        self.question1 = MultipleChoiceQuestion(1, "Multi1", "A")

    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        assert self.c.score_answers(self.question11, [Answer(self.choices)]) \
               == 0


class LonelyMemberCriterion:
    def __init__(self):
        self.choices = "A"
        self.c = LonelyMemberCriterion()
        self.question1 = MultipleChoiceQuestion(1, "Multi1", "A")

    def test_score_answers(self) -> None:
        # only one answer in <answers> and it is valid return 1.0
        assert self.c.score_answers(self.question11, [Answer(self.choices)]) \
               == 0


def test_slice_list(self) -> None:
    assert slice_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def windows(self) -> None:
    assert windows([1, 2, 3], 2) == [[1, 2], [2, 3]]


class TestGroup:
    def __init__(self):
        self.group = grouper.Group([])

    def test_get_members(self) -> None:
        # no member can get
        assert len(self.group.get_members()) == 0


class TestGrouping:
    def __init__(self):
        self.grouping = grouper.Grouping()
        self.group = Group([Student(i, "Student" + str(i)) for i in range(2)])

    def test_add_group(self) -> None:
        assert self.grouping.add_group(self.group)

    def test_get_groups(self) -> None:



class TestSurvey:
    def __init__(self):
        student = course.Student(1, "CSC148")
        question = survey.YesNoQuestion(0, "YesNo")
        student.set_answer(question, survey.Answer(True))
        sur = survey.Survey([question])

    def test_get_questions(self) -> None:
        assert self.sur.get_questions() == []

    def test_get_criterion(self) -> None:


    def test_score_student(self):
        self.sur.set_weight(5, self.question)
        assert self.sur.score_students([self.student]) == 5.0

if __name__ == '__main__':
    import pytest

    pytest.main(['test.py'])
