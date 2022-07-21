import project
import pandas as pd

df = pd.read_csv('test.csv')

def test_get_names():
    output = project.get_names(df)
    expected = ('Sarah', 'Russell')
    assert output == expected


def test_sum_of_cost():
    expected = (29.0, 45.0, 'Sarah', 'Russell', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00', '         shorts $20\nSchool supplies $20\n         co-pay  $5')
    output = project.sum_of_cost(('Sarah', 'Russell'),df)
    assert output == expected


def test_who_owes():
    output = project.who_owes((29.0, 45.0, 'Sarah', 'Russell', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00', '         shorts $20\nSchool supplies $20\n         co-pay  $5'))
    expected =  ('$8.00 is what is owed to Russell.', 'Russell spent $45.00 this month.', 'Sarah spent $29.00 this month.', '         shorts $20\nSchool supplies $20\n         co-pay  $5', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00')
    assert output == expected
