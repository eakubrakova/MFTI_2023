"""��������� �������� ������� ����������� � ����������� �� ������ ��������� 7 ���� ��� ������� ���������������� ���."""

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

from collections import deque

days = deque(maxlen=7)
 
for temp in temps:
    # ��������� ����������� � �������
    days.append(temp)
    # ���� ����� ������� ��������� ������ ������������ ����� ������� (7),
    # �������� ������� ����������� �� ��������� 7 ����
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# ���������� ������ ������, ����� ��������� �������� ���������
# end. ����� ��������� ������ �������� ������������ �� ����������
print("")
