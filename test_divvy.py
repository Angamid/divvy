import project
import pandas as pd

df = pd.read_csv('test.csv')

def test_get_names():
    output = project.get_names(df)
    expected = ('Sarah', 'Romel')
    assert output == expected


def test_sum_of_cost():
    expected = (29.0, 45.0, 'Sarah', 'Romel', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00', '         shorts $20\nSchool supplies $20\n         co-pay  $5')
    output = project.sum_of_cost(('Sarah', 'Romel'),df)
    assert output == expected


def test_who_owes():
    output = project.who_owes((29.0, 45.0, 'Sarah', 'Romel', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00', '         shorts $20\nSchool supplies $20\n         co-pay  $5'))
    expected =  ('$8.00 is what is owed to Romel.', 'Romel spent $45.00 this month.', 'Sarah spent $29.00 this month.', '         shorts $20\nSchool supplies $20\n         co-pay  $5', '       Vitamins    $15\nDriving 12miles     $2\n       Medicine $12.00')
    assert output == expected
