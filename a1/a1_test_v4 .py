import course
import survey
import criterion
import grouper
import pytest

from typing import List, Set

logo = '''
   _____                          _    _       _
  / ____|                        | |  | |     (_)
 | (___   __ ___   ____   ___   _| |  | |_ __  _
  \\___ \\ / _` \\ \\ / /\\ \\ / / | | | |  | | '_ \\| |
  ____) | (_| |\\ V /  \\ V /| |_| | |__| | | | | |
 |_____/ \\__,_| \\_/    \\_/  \\__, |\\____/|_| |_|_|
                             __/ |
                            |___/
'''

disclaimer = u'''
\u0053\u0061\u0076\u0076\u0079\u0055\u006e\u0069\u0020\u0058\u0020\u4e00\u52fe\u0043\u0053\u5927\u8bfe\u5802\u5b66\u751f\u4f7f\u7528\u000d\u000a\u5206\u4eab\u5bb6\u7834\u4eba\u4ea1\u000d\u000a\u672a\u7ecf\u6388\u6743\u4f7f\u7528\u5bb6\u7834\u4eba\u4ea1\u000d\u000a\u003a\u0020\u0029\u000d\u000a\u000d\u000a\u0030\u002e\u0020\u8bf7\u4f60\u4e0d\u8981\u5206\u4eab\uff0c\u8bf7\u4e0d\u662f\u6211\u5b66\u751f\u7684\u4eba\u4e0d\u8981\u76d7\u7528\uff0c\u505a\u4e2a\u4eba\u5427\uff0c\u5c0a\u91cd\u522b\u4eba\u7684\u52b3\u52a8\u5427\u000d\u000a\u0031\u002e\u0020\u6211\u7684\u0074\u0065\u0073\u0074\u0073\u6db5\u76d6\u4e86\u6700\u57fa\u672c\u7684\u9898\u76ee\u8981\u6c42\u548c\u4e00\u4e9b\u6bd4\u8f83\u590d\u6742\u7684\u60c5\u51b5\uff0c\u6bd4\u5b66\u6821\u8001\u5e08\u7ed9\u7684\u0074\u0065\u0073\u0074\u0073\u60c5\u51b5\u8981\u591a\u4e0d\u5c11\uff0c\u4f46\u662f\u72b9\u8c6b\u672c\u8eab\u4f5c\u4e1a\u903b\u8f91\u4e5f\u6bd4\u8f83\u590d\u6742\uff0c\u6240\u4ee5\u5e76\u4e0d\u4ee3\u8868\u8fc7\u4e86\u6211\u7684\u0074\u0065\u0073\u0074\u0073\u4f60\u5c31\u53ef\u4ee5\u62ff\u5230\u0063\u006f\u0072\u0072\u0065\u0063\u0074\u006e\u0065\u0073\u0073\u6ee1\u5206\u000d\u000a\u0032\u002e\u0020\u8bf7\u4f60\u5b66\u6211\u7684\u0074\u0065\u0073\u0074\u0073\uff0c\u518d\u81ea\u5df1\u6dfb\u52a0\u66f4\u591a\u66f4\u590d\u6742\u7684\u60c5\u51b5\u000d\u000a\u0033\u002e\u0020\u4e0a\u8bfe\u6211\u4f1a\u6559\u4f60\u5982\u4f55\u5229\u7528\u8fd9\u4e2a\u6587\u4ef6\u6765\u0064\u0065\u0062\u0075\u0067\u000d\u000a\u0034\u002e\u0020\u5982\u679c\u4f60\u6709\u4e00\u5929\u5de5\u4f5c\u4e86\u4f60\u5c31\u77e5\u9053\u5199\u0074\u0065\u0073\u0074\u0073\u6d4b\u8bd5\u4ee3\u7801\u662f\u6709\u591a\u67af\u71e5\u591a\u9ebb\u70e6\u591a\u8ba9\u4eba\u6293\u72c2\u7684\u4e8b\u60c5\u4e86\uff0c\u6240\u4ee5\u73cd\u60dc\u5f53\u4e0b'''


def fuck_within(actual, expected, delta=0.001):
    return expected - delta <= actual <= expected + delta


def fuck_compare_lists(actual, expect):
    return set(actual) == set(expect)

#####################################
# Fake classes and tests for Step 2
#####################################


class FakeQuestion:
    def __init__(self, id_, text):
        self.id = id_
        self.text = text

    def validate_answer(self, ans):
        # fake code, up to answer to tell us if it's valid
        return ans.valid


class FakeAnswer:
    def __init__(self, valid):
        self.valid = valid

    def is_valid(self, question) -> bool:
        return self.valid


class TestStep2:
    def test_student_class(self):
        s = course.Student(0, "Shit")
        assert s.id == 0
        assert s.name == "Shit"
        assert str(s) == "Shit"

        q1 = FakeQuestion(1, "Fuck!")
        q2 = FakeQuestion(2, "Fuck!!")
        assert not s.has_answer(q1), 'no answer currently'
        assert not s.has_answer(q2), 'no answer currently'

        s.set_answer(q1, FakeAnswer(False))
        s.set_answer(q2, FakeAnswer(True))

        assert not s.has_answer(q1), """we did add an answer for q1 but it's not valid"""
        assert s.has_answer(q2)
        assert s.get_answer(q1) is not None
        assert s.get_answer(q2) is not None

#####################################
# Fake classes and tests for Step 3
#####################################


class TestStep3:
    def test_course_simple(self):
        c = course.Course("SHIT101")
        assert c.name == 'SHIT101'

        # Note that we cannot test all_answered at this point
        # since Survey is not yet implemented at step 3

        # everything should be empty at this point
        assert c.students == []
        assert c.get_students() == ()

    def test_course_complex(self):
        c = course.Course("SHIT101")

        c.enroll_students([])

        # enroll empty list, got empty
        assert c.students == []
        assert c.get_students() == ()

        # add one student
        c.enroll_students([course.Student(0, "FUCK0")])
        assert len(c.students) == 1
        assert [(x.id, x.name) for x in c.students] == [(0, 'FUCK0')]
        assert len(c.get_students()) == 1
        assert isinstance(c.get_students(), tuple)
        assert [(x.id, x.name) for x in c.get_students()] == [(0, 'FUCK0')]

        # add same student again should not change anything
        c.enroll_students([course.Student(0, "FUCK0")])
        assert len(c.students) == 1
        assert [(x.id, x.name) for x in c.students] == [(0, 'FUCK0')]
        assert len(c.get_students()) == 1
        assert isinstance(c.get_students(), tuple)
        assert [(x.id, x.name) for x in c.get_students()] == [(0, 'FUCK0')]

        # add student with empty name should not change anything
        c.enroll_students([course.Student(888, "")])
        assert len(c.students) == 1
        assert [(x.id, x.name) for x in c.students] == [(0, 'FUCK0')]
        assert len(c.get_students()) == 1
        assert isinstance(c.get_students(), tuple)
        assert [(x.id, x.name) for x in c.get_students()] == [(0, 'FUCK0')]

        # add some more
        c.enroll_students([course.Student(2, "FUCK2"), course.Student(1, "FUCK1"), course.Student(99, "FUCK99")])
        assert len(c.students) == 4
        assert len(c.get_students()) == 4
        assert isinstance(c.get_students(), tuple)
        assert [(x.id, x.name) for x in c.get_students()] == [(0, 'FUCK0'), (1, 'FUCK1'), (2, 'FUCK2'), (99, 'FUCK99')]

        # add some more, but contains invalid student, should change nothing
        c.enroll_students([course.Student(2, "FUCK2"),
                           course.Student(0, "FUCK0"),
                           course.Student(88, "FUCK88"),
                           course.Student(99, "FUCK99")])
        assert len(c.students) == 4
        assert len(c.get_students()) == 4
        assert isinstance(c.get_students(), tuple)
        assert [(x.id, x.name) for x in c.get_students()] == [(0, 'FUCK0'),
                                                              (1, 'FUCK1'),
                                                              (2, 'FUCK2'),
                                                              (99, 'FUCK99')]

#####################################
# Fake classes and tests for Step 4
# Please note we cannot test is_valid_answer at this point
# since I don't know exactly how you wish to implement it
#####################################


class FakeAnswer2:
    def __init__(self, x):
        self.content = x


class TestStep4:
    def test_multiple_choice(self):
        m = survey.MultipleChoiceQuestion(0, "just choose", ["A", "B", "C"])
        assert m.id == 0
        assert m.text == 'just choose'
        assert 'just choose' in str(m)
        assert 'A' in str(m)
        assert 'B' in str(m)
        assert 'C' in str(m)
        assert m.get_similarity(FakeAnswer2("X"), FakeAnswer2("X")) == 1.0
        assert m.get_similarity(FakeAnswer2("X"), FakeAnswer2("Y")) == 0.0

    def test_checkbox(self):
        m = survey.CheckboxQuestion(0, "just choose", ["A", "B", "C", "D", "E", "F"])
        assert m.id == 0
        assert m.text == 'just choose'
        assert 'just choose' in str(m)
        assert 'A' in str(m)
        assert 'B' in str(m)
        assert 'C' in str(m)
        assert m.get_similarity(FakeAnswer2(["A"]), FakeAnswer2(["A"])) == 1.0
        assert m.get_similarity(FakeAnswer2(["A", "B"]), FakeAnswer2(["A", "B"])) == 1.0
        assert fuck_within(m.get_similarity(FakeAnswer2(["A", "B"]), FakeAnswer2(["A", "B", "C"])), 0.6666666)
        assert fuck_within(m.get_similarity(FakeAnswer2(["A", "B", "C"]), FakeAnswer2(["A", "B"])), 0.6666666)
        assert fuck_within(m.get_similarity(FakeAnswer2(["C", "A", "B"]), FakeAnswer2(["A", "B"])), 0.6666666)
        assert m.get_similarity(FakeAnswer2(["A", "C", "D", "E"]), FakeAnswer2(["A", "B"])) == 0.2

    def test_true_false(self):
        m = survey.YesNoQuestion(0, "yue?")
        assert m.id == 0
        assert m.text == 'yue?'
        assert 'yue?' in str(m)
        assert m.get_similarity(FakeAnswer2(True), FakeAnswer2(True)) == 1.0
        assert m.get_similarity(FakeAnswer2(False), FakeAnswer2(False)) == 1.0
        assert m.get_similarity(FakeAnswer2(True), FakeAnswer2(False)) == 0.0
        assert m.get_similarity(FakeAnswer2(False), FakeAnswer2(True)) == 0.0

    def test_numeric(self):
        m = survey.NumericQuestion(0, "what's my number", 5, 10)
        assert m.id == 0
        assert m.text == "what's my number"
        assert "what's my number" in str(m)
        assert '5' in str(m)
        assert '10' in str(m)
        assert m.get_similarity(FakeAnswer2(5), FakeAnswer2(5)) == 1.0
        assert fuck_within(m.get_similarity(FakeAnswer2(6), FakeAnswer2(7)), 0.8)
        assert m.get_similarity(FakeAnswer2(5), FakeAnswer2(10)) == 0.0
        assert m.get_similarity(FakeAnswer2(5), FakeAnswer2(5)) == 1.0
        assert m.get_similarity(FakeAnswer2(10), FakeAnswer2(10)) == 1.0


#####################################
# Fake classes and tests for Step 5
# now we can test is_valid_answer
#####################################


class TestStep5:

    def test_answer_simple(self):
        a1 = survey.Answer("A")
        assert a1.content == 'A'

    def test_multiple_choice(self):
        q1 = survey.MultipleChoiceQuestion(0, "just choose", ["A", "B", "C"])
        assert not q1.validate_answer(survey.Answer(1))
        assert not q1.validate_answer(survey.Answer("E"))
        assert not q1.validate_answer(survey.Answer(True))
        assert not q1.validate_answer(survey.Answer(False))
        assert not q1.validate_answer(survey.Answer(4))
        assert not q1.validate_answer(survey.Answer(["A", "B", "C"]))
        assert q1.validate_answer(survey.Answer("A"))
        assert q1.validate_answer(survey.Answer("B"))
        assert q1.validate_answer(survey.Answer("C"))

        assert not survey.Answer(1).is_valid(q1)
        assert not survey.Answer("E").is_valid(q1)
        assert not survey.Answer(True).is_valid(q1)
        assert not survey.Answer(False).is_valid(q1)
        assert not survey.Answer(["A", "B", "C"]).is_valid(q1)
        assert survey.Answer("A").is_valid(q1)
        assert survey.Answer("B").is_valid(q1)
        assert survey.Answer("C").is_valid(q1)

    def test_checkbox(self):
        q1 = survey.CheckboxQuestion(0, "just choose", ["A", "B", "C", "D", "E", "F"])
        assert not q1.validate_answer(survey.Answer(1))
        assert not q1.validate_answer(survey.Answer("E"))
        assert not q1.validate_answer(survey.Answer(True))
        assert not q1.validate_answer(survey.Answer(False))
        assert not q1.validate_answer(survey.Answer(4))
        assert not q1.validate_answer(survey.Answer(["A", "B", "C", "G"]))
        assert q1.validate_answer(survey.Answer(["A"]))
        assert q1.validate_answer(survey.Answer(["B", "A"]))
        assert q1.validate_answer(survey.Answer(["A", "C", "B", "D", "E", "F"]))

        assert not survey.Answer(1).is_valid(q1)
        assert not survey.Answer("E").is_valid(q1)
        assert not survey.Answer(True).is_valid(q1)
        assert not survey.Answer(False).is_valid(q1)
        assert not survey.Answer(["A", "B", "C", "G"]).is_valid(q1)
        assert survey.Answer(["A"]).is_valid(q1)
        assert survey.Answer(["B", "A"]).is_valid(q1)
        assert survey.Answer(["A", "B", "C", "D", "E", "F"]).is_valid(q1)
        assert survey.Answer(["A", "C", "B", "D", "E", "F"]).is_valid(q1)

    def test_yes_no(self):
        q1 = survey.YesNoQuestion(0, "yue?")
        assert not q1.validate_answer(survey.Answer(1))
        assert not q1.validate_answer(survey.Answer("E"))
        assert not q1.validate_answer(survey.Answer(4))
        assert not q1.validate_answer(survey.Answer(["A", "B", "C"]))
        assert q1.validate_answer(survey.Answer(True))
        assert q1.validate_answer(survey.Answer(False))

        assert not survey.Answer(1).is_valid(q1)
        assert not survey.Answer("E").is_valid(q1)
        assert not survey.Answer(["A", "B", "C"]).is_valid(q1)
        assert survey.Answer(True).is_valid(q1)
        assert survey.Answer(False).is_valid(q1)

    def test_numeric(self):
        q1 = survey.NumericQuestion(0, "what's my number", 5, 10)
        assert not q1.validate_answer(survey.Answer(1))
        assert not q1.validate_answer(survey.Answer("E"))
        assert not q1.validate_answer(survey.Answer(True))
        assert not q1.validate_answer(survey.Answer(False))
        assert not q1.validate_answer(survey.Answer(15))
        assert not q1.validate_answer(survey.Answer(["A", "B", "C"]))
        assert q1.validate_answer(survey.Answer(5))
        assert q1.validate_answer(survey.Answer(8))
        assert q1.validate_answer(survey.Answer(10))

        assert not survey.Answer(1).is_valid(q1)
        assert not survey.Answer("E").is_valid(q1)
        assert not survey.Answer(True).is_valid(q1)
        assert not survey.Answer(False).is_valid(q1)
        assert not survey.Answer(["A", "B", "C"]).is_valid(q1)
        assert not survey.Answer(15).is_valid(q1)
        assert survey.Answer(5).is_valid(q1)
        assert survey.Answer(8).is_valid(q1)
        assert survey.Answer(10).is_valid(q1)

    def test_student(self):
        s = course.Student(0, "Shit")
        q1 = survey.NumericQuestion(0, "what's my number", 5, 10)
        assert s.get_answer(q1) is None
        assert not s.has_answer(q1)

        s.set_answer(q1, survey.Answer(False))
        assert s.get_answer(q1) is not None, '''get_answer should return the answer even it's not valid '''
        assert not s.has_answer(q1), ''' has answer will be false if answer not valid'''

        s.set_answer(q1, survey.Answer(5))
        assert s.get_answer(q1) is not None
        assert s.has_answer(q1)

        s.set_answer(q1, survey.Answer(8))
        assert s.get_answer(q1) is not None
        assert s.has_answer(q1)

        s.set_answer(q1, survey.Answer(10))
        assert s.get_answer(q1) is not None
        assert s.has_answer(q1)


#####################################
# Fake classes and tests for Step 6
# Criterion
#####################################

class TestStep6:
    def test_homo_mc(self):
        c = criterion.HomogeneousCriterion()
        q = survey.MultipleChoiceQuestion(0, "Shit", ["A", "B", "C"])
        a1 = survey.Answer("A")
        a2 = survey.Answer("B")
        a3 = survey.Answer("C")
        assert c.score_answers(q, [a1]) == 1.0, '''single answer should result in 1'''
        assert c.score_answers(q, [a1, a2]) == 0
        assert fuck_within(c.score_answers(q, [a1, a1, a1]), 1)
        assert fuck_within(c.score_answers(q, [a1, a2, a1]), 0.33333)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a3]), 0.166666)

    def test_heter_mc(self):
        c = criterion.HeterogeneousCriterion()
        q = survey.MultipleChoiceQuestion(0, "Shit", ["A", "B", "C"])
        a1 = survey.Answer("A")
        a2 = survey.Answer("B")
        a3 = survey.Answer("C")
        assert c.score_answers(q, [a1]) == 0.0, '''single answer should result in 0'''
        assert c.score_answers(q, [a1, a2]) == 1
        assert fuck_within(c.score_answers(q, [a1, a1, a1]), 0)
        assert fuck_within(c.score_answers(q, [a1, a2, a1]), 1 - 0.33333)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a3]), 1 - 0.166666)

    def test_lonely_mc(self):
        c = criterion.LonelyMemberCriterion()
        q = survey.MultipleChoiceQuestion(0, "Shit", ["A", "B", "C"])
        a1 = survey.Answer("A")
        a2 = survey.Answer("B")
        a3 = survey.Answer("C")
        assert q.get_similarity(a1, a1) != 0.0
        assert c.score_answers(q, [a1]) == 0.0, '''single answer should result in 0'''
        assert c.score_answers(q, [a1, a2]) == 0.0
        assert fuck_within(c.score_answers(q, [a1, a1, a1]), 1)
        assert fuck_within(c.score_answers(q, [a1, a1, a2, a2]), 1)
        assert fuck_within(c.score_answers(q, [a1, a2, a1]), 0)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a3]), 0)
        assert fuck_within(c.score_answers(q, [a1, a1, a1, a2, a2]), 1)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a1, a2, a3]), 0)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a1, a2, a3, a3]), 1)

    def test_homo_numeric(self):
        c = criterion.HomogeneousCriterion()
        q = survey.NumericQuestion(0, "OH Shit", 2, 8)
        a1 = survey.Answer(2)
        a2 = survey.Answer(5)
        a3 = survey.Answer(7)
        assert c.score_answers(q, [a1]) == 1.0, '''single answer should result in 1'''
        assert fuck_within(c.score_answers(q, [a1, a2]), 0.5)
        assert fuck_within(c.score_answers(q, [a1, a1, a2]), 0.66666666)
        assert fuck_within(c.score_answers(q, [a1, a2, a3]), 0.44444444)

        # This is to test you throw an exception when one answer is not valid
        a4 = survey.Answer(10)
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a4])
        assert info
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a1, a2, a4])
        assert info

    def test_heter_numeric(self):
        c = criterion.HeterogeneousCriterion()
        q = survey.NumericQuestion(0, "OH Shit", 2, 8)
        a1 = survey.Answer(2)
        a2 = survey.Answer(5)
        a3 = survey.Answer(7)
        assert c.score_answers(q, [a1]) == 0.0, '''single answer should result in 0'''
        assert fuck_within(c.score_answers(q, [a1, a2]), 0.5)
        assert fuck_within(c.score_answers(q, [a1, a1, a2]), 0.33333333)
        assert fuck_within(c.score_answers(q, [a1, a2, a3]), 0.55555555)

        # This is to test you throw an exception when one answer is not valid
        a4 = survey.Answer(10)
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a4])
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a1, a2, a4])
        assert info

    def test_lonely_numeric(self):
        c = criterion.LonelyMemberCriterion()
        q = survey.NumericQuestion(0, "OH Shit", 2, 8)
        a1 = survey.Answer(2)
        a2 = survey.Answer(5)
        a3 = survey.Answer(7)
        assert q.get_similarity(a1, a1) != 0.0
        assert c.score_answers(q, [a1]) == 0.0, '''single answer should result in 0'''
        assert c.score_answers(q, [a1, a2]) == 0.0
        assert fuck_within(c.score_answers(q, [a1, a1, a1]), 1)
        assert fuck_within(c.score_answers(q, [a1, a1, a2, a2]), 1)
        assert fuck_within(c.score_answers(q, [a1, a2, a1]), 0)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a3]), 0)
        assert fuck_within(c.score_answers(q, [a1, a1, a1, a2, a2]), 1)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a1, a2, a3]), 0)
        assert fuck_within(c.score_answers(q, [a1, a2, a1, a1, a2, a3, a3]), 1)

        # This is to test you throw an exception when one answer is not valid
        a4 = survey.Answer(10)

        # first answer is invalid
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a4, a1, a2])
        assert info

        # last answer is invalid
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a4])
        with pytest.raises(criterion.InvalidAnswerError) as info:
            c.score_answers(q, [a1, a2, a4])
        assert info, 'if you fail this test, maybe your code return too early'


#####################################
# Fake classes and tests for Step 7
# Group
#####################################

class TestStep7:
    def test_simple(self):
        g = grouper.Group([])
        students = [course.Student(i, "Shit" + str(i)) for i in range(10)]

        assert g.get_members() == []
        assert len(g) == 0
        assert students[0] not in g

        g = grouper.Group(students)
        assert len(g) == 10
        for i in range(10):
            assert students[i] in g
            assert students[i].name in str(g)
        assert isinstance(g.get_members(), list)
        assert len(g.get_members()) == 10

        # mutate shallow copy should not affect original list in Group
        members = g.get_members()
        members.append(course.Student(100, 'ok'))

        assert len(g) == 10
        for i in range(10):
            assert students[i] in g
            assert students[i].name in str(g)
        assert isinstance(g.get_members(), list)
        assert len(g.get_members()) == 10


#####################################
# Fake classes and tests for Step 8
# Grouping
#####################################

class TestStep8:
    def test_simple(self):
        g = grouper.Grouping()
        assert len(g) == 0
        assert str(g) is not None

    def test_get_groups_shallow(self):
        g = grouper.Grouping()
        L = g.get_groups()
        assert len(L) == 0
        L.append(4)
        assert g.get_groups() == []

    def test_add_group(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(10)]
        g = grouper.Grouping()
        assert g.add_group(grouper.Group([students[0], students[1]]))
        assert len(g) == 1
        assert len(g.get_groups()) == 1

        # you cannot add empty group
        assert not g.add_group(grouper.Group([]))
        assert len(g) == 1
        assert len(g.get_groups()) == 1

        # you cannot add group contains students already exist in group
        assert not g.add_group(grouper.Group([students[1], students[2]]))
        assert len(g) == 1
        assert len(g.get_groups()) == 1

        # you can add another group
        assert g.add_group(grouper.Group([students[2], students[3]]))
        assert len(g) == 2
        assert len(g.get_groups()) == 2

        members = [x.get_members() for x in g.get_groups()]
        flat_list = [item for sublist in members for item in sublist]
        ids = set([x.id for x in flat_list])
        assert ids == {0, 1, 2, 3}

        # you can add another group
        assert g.add_group(grouper.Group([students[7], students[8]]))
        assert len(g) == 3
        assert len(g.get_groups()) == 3

        members = [x.get_members() for x in g.get_groups()]
        flat_list = [item for sublist in members for item in sublist]
        ids = set([x.id for x in flat_list])
        assert ids == {0, 1, 2, 3, 7, 8}


#####################################
# Fake classes and tests for Step 9
# Survey
#####################################

class TestStep9:
    def test_empty_survey(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(10)]
        q1 = survey.YesNoQuestion(0, "Yue me?")
        s = survey.Survey([])
        assert len(s) == 0
        assert q1 not in s
        assert str(s) is not None
        assert len(s.get_questions()) == 0
        assert s.get_questions() == []
        assert isinstance(s._get_criterion(q1), criterion.HomogeneousCriterion)
        assert isinstance(s._get_weight(q1), int)
        assert s.score_students(students) == 0

    def test_weight_crit(self):
        stu = course.Student(0, "Shit0")
        q = survey.YesNoQuestion(0, "Yue me?")
        stu.set_answer(q, survey.Answer(True))
        s = survey.Survey([q])
        assert s.score_students([stu]) == 1.0
        s.set_weight(5, q)
        assert s.score_students([stu]) == 5.0
        s.set_criterion(criterion.HeterogeneousCriterion(), q)
        assert s.score_students([stu]) == 0.0

    def test_complicated(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(3)]
        questions1 = [survey.NumericQuestion(i, "FUCKNQ" + str(i), 2, 8) for i in range(5)]
        s = survey.Survey(questions1)
        assert len(s) == 5
        assert questions1[0] in s
        assert survey.YesNoQuestion(99, "Yue?") not in s
        assert str(s).count("FUCKNQ") >= 5
        assert len(s.get_questions()) == 5
        assert fuck_compare_lists([x.id for x in s.get_questions()], [0, 1, 2, 3, 4])

        answers = [0, 1, 0, 1, 2] * 3
        i = 0
        for q in questions1:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1
        assert fuck_within(s.score_students(students), 0.8222222)

        answers = [1, 0, 0, 3, 4] * 3
        i = 0
        for q in questions1:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1
        assert fuck_within(s.score_students(students), 0.6666666666666667)

        s.set_weight(2, questions1[0])
        assert fuck_within(s.score_students(students), 0.8444444444444444)

        s.set_criterion(criterion.HeterogeneousCriterion(), questions1[1])
        assert fuck_within(s.score_students(students), 0.7777777777777779)

        # this should result in InvalidAnswerError
        answers = [9, 9, 9, 9, 9] * 3
        i = 0
        for q in questions1:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1
        assert fuck_within(s.score_students(students), 0)

        assert s.score_grouping(grouper.Grouping()) == 0, '''empty grouping result always 1'''
        g = grouper.Grouping()
        g.add_group(grouper.Group([students[0]]))
        g.add_group(grouper.Group([students[1]]))
        g.add_group(grouper.Group([students[2]]))
        assert s.score_students([students[0]]) == 0
        assert s.score_students([students[1]]) == 0
        assert s.score_students([students[2]]) == 0
        assert s.score_grouping(g) == 0

        answers = [1, 0, 0, 3, 4] * 3
        i = 0
        for q in questions1:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1
        assert s.score_grouping(g) == 1.0

    def test_super_complicated(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(8)]
        q1 = survey.YesNoQuestion(0, "To be, or not to be")
        q2 = survey.NumericQuestion(1, "How many times you fuck up", 0, 10000)
        q3 = survey.MultipleChoiceQuestion(2, "What's your favorite thing to do", ['A', 'B', 'C', 'D'])
        q4 = survey.CheckboxQuestion(3, "How many things you have done", ['A', 'B', 'C', 'D', 'E'])
        questions = [q1, q2, q3, q4]
        s = survey.Survey(questions)

        answers = [True, 1111, 'A', ['A', 'C'],
                   False, 44, 'C', ['A', 'B', 'C'],
                   True, 3, 'B', ['A', 'C', 'D'],
                   True, 56, 'C', ['D', 'C'],
                   False, 12, 'C', ['E'],
                   True, 0, 'A', ['A'],
                   False, 888, 'C', ['A', 'B', 'C', 'D'],
                   True, 12, 'B', ['A', 'B', 'C', 'D', 'E']]

        i = 0
        for stu in students:
            for q in questions:
                stu.set_answer(q, survey.Answer(answers[i]))
                i += 1
        g = grouper.Grouping()
        g.add_group(grouper.Group([students[0], students[1], students[2]]))
        g.add_group(grouper.Group([students[3], students[4], students[5]]))
        g.add_group(grouper.Group([students[6], students[7]]))
        assert fuck_within(s.score_students(students), 0.5175303571428571)
        assert fuck_within(s.score_grouping(g), 0.43715925925925925)

        s.set_weight(2, q2)
        s.set_weight(5, q1)
        s.set_weight(6, q3)
        s.set_weight(3, q4)
        assert fuck_within(s.score_students(students), 1.7600607142857143)
        assert fuck_within(s.score_grouping(g), 1.2696888888888889)

        s.set_criterion(criterion.HeterogeneousCriterion(), q1)
        s.set_criterion(criterion.HeterogeneousCriterion(), q2)
        s.set_criterion(criterion.HeterogeneousCriterion(), q3)
        s.set_criterion(criterion.HeterogeneousCriterion(), q4)
        assert fuck_within(s.score_students(students), 2.2399392857142857)
        assert fuck_within(s.score_grouping(g), 2.7303111111111114)


#####################################
# Fake classes and tests for Step 10
# Helpers
#####################################

class TestStep10:
    def test_slicing(self):
        assert grouper.slice_list([], 2) == []
        assert grouper.slice_list([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
        assert grouper.slice_list([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]
        assert grouper.slice_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
        assert grouper.slice_list([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
        assert grouper.slice_list([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]

    def test_windows(self):
        assert grouper.windows([], 2) == []
        assert grouper.windows([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
        assert grouper.windows([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        assert grouper.windows([1, 2, 3, 4, 5], 2) == [[1, 2], [2, 3], [3, 4], [4, 5]]
        assert grouper.windows([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
        assert grouper.windows([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


#####################################
# Fake classes and tests for Step 10
# Grouper
#####################################

def grouping_to_list_of_list(grouping: grouper.Grouping):
    r = []
    for g in grouping.get_groups():
        r.append(sorted([x.id for x in g.get_members()]))
    r.sort()
    return r


def grouping_to_list_of_list_flatten(grouping: grouper.Grouping):
    r = []
    for g in grouping.get_groups():
        r.extend([x.id for x in g.get_members()])
    r.sort()
    return r


class TestStep10:

    def test_alpha(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "FUCKNQ" + str(i), 2, 8) for i in range(5)]
        s = survey.Survey(questions)

        answers = [1, 0, 0, 3, 4] * 5
        i = 0
        for q in questions:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1

        c = course.Course("Asshole101")
        c.enroll_students(students)

        grouping1 = grouper.AlphaGrouper(1).make_grouping(c, s)
        assert len(grouping1) == 5
        assert grouping_to_list_of_list(grouping1) == [[0], [1], [2], [3], [4]]

        grouping2 = grouper.AlphaGrouper(2).make_grouping(c, s)
        assert len(grouping2) == 3
        assert grouping_to_list_of_list(grouping2) == [[0, 1], [2, 3], [4]]

        grouping3 = grouper.AlphaGrouper(3).make_grouping(c, s)
        assert len(grouping3) == 2
        assert grouping_to_list_of_list(grouping3) == [[0, 1, 2], [3, 4]]

        grouping5 = grouper.AlphaGrouper(5).make_grouping(c, s)
        assert len(grouping5) == 1
        assert grouping_to_list_of_list(grouping5) == [[0, 1, 2, 3, 4]]

    def test_random(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "FUCKNQ" + str(i), 2, 8) for i in range(5)]
        s = survey.Survey(questions)

        answers = [1, 0, 0, 3, 4] * 5
        i = 0
        for q in questions:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1

        c = course.Course("Asshole101")
        c.enroll_students(students)

        grouping1 = grouper.RandomGrouper(1).make_grouping(c, s)
        assert len(grouping1) == 5
        assert grouping_to_list_of_list_flatten(grouping1) == [0, 1, 2, 3, 4]

        grouping2 = grouper.RandomGrouper(2).make_grouping(c, s)
        assert len(grouping2) == 3
        assert grouping_to_list_of_list_flatten(grouping2) == [0, 1, 2, 3, 4]

        grouping3 = grouper.RandomGrouper(3).make_grouping(c, s)
        assert len(grouping3) == 2
        assert grouping_to_list_of_list_flatten(grouping3) == [0, 1, 2, 3, 4]

        grouping5 = grouper.RandomGrouper(5).make_grouping(c, s)
        assert len(grouping5) == 1
        assert grouping_to_list_of_list_flatten(grouping5) == [0, 1, 2, 3, 4]

    def test_greedy(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "FUCKNQ" + str(i), 2, 8) for i in range(5)]
        s = survey.Survey(questions)

        answers = [1, 0, 0, 3, 4, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 1, 0, 1, 3, 0, 0, 3, 2]
        i = 0
        for q in questions:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1

        c = course.Course("Asshole101")
        c.enroll_students(students)

        grouping1 = grouper.GreedyGrouper(1).make_grouping(c, s)
        assert len(grouping1) == 5
        assert grouping_to_list_of_list(grouping1) == [[0], [1], [2], [3], [4]]

        grouping2 = grouper.GreedyGrouper(2).make_grouping(c, s)
        assert len(grouping2) == 3
        assert grouping_to_list_of_list(grouping2) == [[0, 3], [1, 2], [4]]

        grouping3 = grouper.GreedyGrouper(3).make_grouping(c, s)
        assert len(grouping3) == 2
        assert grouping_to_list_of_list(grouping3) == [[0, 3, 4], [1, 2]]

        grouping5 = grouper.GreedyGrouper(5).make_grouping(c, s)
        assert len(grouping5) == 1
        assert grouping_to_list_of_list(grouping5) == [[0, 1, 2, 3, 4]]

    def test_window(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(5)]
        questions = [survey.NumericQuestion(i, "FUCKNQ" + str(i), 2, 8) for i in range(5)]
        s = survey.Survey(questions)

        answers = [1, 0, 0, 3, 4, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 1, 0, 1, 3, 0, 0, 3, 2]
        i = 0
        for q in questions:
            for stu in students:
                stu.set_answer(q, survey.Answer(2 + answers[i]))
                i += 1

        c = course.Course("Asshole101")
        c.enroll_students(students)

        grouping1 = grouper.WindowGrouper(1).make_grouping(c, s)
        assert len(grouping1) == 5
        assert grouping_to_list_of_list(grouping1) == [[0], [1], [2], [3], [4]]

        grouping2 = grouper.WindowGrouper(2).make_grouping(c, s)
        assert len(grouping2) == 3
        assert grouping_to_list_of_list(grouping2) == [[0], [1, 2], [3, 4]]

        grouping3 = grouper.WindowGrouper(3).make_grouping(c, s)
        assert len(grouping3) == 2
        assert grouping_to_list_of_list(grouping3) == [[0, 1, 2], [3, 4]]

        grouping5 = grouper.WindowGrouper(5).make_grouping(c, s)
        assert len(grouping5) == 1
        assert grouping_to_list_of_list(grouping5) == [[0, 1, 2, 3, 4]]

    def test_combination(self):
        students = [course.Student(i, "Shit" + str(i)) for i in range(8)]
        q1 = survey.YesNoQuestion(0, "To be, or not to be")
        q2 = survey.NumericQuestion(1, "How many times you fuck up", 0, 10000)
        q3 = survey.MultipleChoiceQuestion(2, "What's your favorite thing to do", ['A', 'B', 'C', 'D'])
        q4 = survey.CheckboxQuestion(3, "How many things you have done", ['A', 'B', 'C', 'D', 'E'])
        questions = [q1, q2, q3, q4]
        s = survey.Survey(questions)

        answers = [True, 1111, 'A', ['A', 'C'],
                   False, 44, 'C', ['A', 'B', 'C'],
                   True, 3, 'B', ['A', 'C', 'D'],
                   True, 56, 'C', ['D', 'C'],
                   False, 12, 'C', ['E'],
                   True, 0, 'A', ['A'],
                   False, 888, 'C', ['A', 'B', 'C', 'D'],
                   True, 12, 'B', ['A', 'B', 'C', 'D', 'E']]

        i = 0
        for stu in students:
            for q in questions:
                stu.set_answer(q, survey.Answer(answers[i]))
                i += 1

        c = course.Course("Asshole101")
        c.enroll_students(students)

        grouping = grouper.AlphaGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]

        grouping = grouper.GreedyGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 2, 5], [1, 4, 6], [3, 7]]

        grouping = grouper.WindowGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 4, 5], [1, 2, 3], [6, 7]]

        s.set_criterion(criterion.HeterogeneousCriterion(), q2)
        s.set_weight(2, q1)
        s.set_weight(2, q1)
        s.set_weight(3, q2)
        s.set_weight(55, q4)

        grouping = grouper.AlphaGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]

        grouping = grouper.GreedyGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 2, 6], [1, 3, 7], [4, 5]]

        grouping = grouper.WindowGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4], [5, 6, 7]]

        s.set_weight(2, q1)
        s.set_weight(1, q2)
        s.set_weight(5, q3)
        s.set_weight(2, q4)
        s.set_criterion(criterion.LonelyMemberCriterion(), q1)
        s.set_criterion(criterion.LonelyMemberCriterion(), q2)
        s.set_criterion(criterion.LonelyMemberCriterion(), q3)
        s.set_criterion(criterion.LonelyMemberCriterion(), q4)

        grouping = grouper.AlphaGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]

        grouping = grouper.GreedyGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 2, 5], [1, 4, 6], [3, 7]]

        grouping = grouper.WindowGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]

        # make one of the student's answer invalid
        students[0].set_answer(q1, survey.Answer('FUCK'))

        grouping = grouper.AlphaGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]

        grouping = grouper.GreedyGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 6], [5, 7]]

        grouping = grouper.WindowGrouper(3).make_grouping(c, s)
        assert len(grouping) == 3
        assert grouping_to_list_of_list(grouping) == [[0, 1, 2], [3, 4, 5], [6, 7]]


if __name__ == '__main__':
    print(logo)
    print(disclaimer)
    pytest.main(['a1_shittests_v4.py'])
