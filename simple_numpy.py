import numpy as np

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

# �������� ������� ������ � ����������� � np.nan � ������� mystery
# True - �������� ���������, False - �������� �� ���������
nans_index = np.isnan(mystery)

# � ���������� n_nan ��������� ����� ����������� ��������
n_nan = sum(nans_index)

# ���������� ������ `mystery` � ������ `mystery_new`. ��������� ����������� 
# �������� � ������� `mystery_new` ������
mystery_new = mystery.copy()
mystery_new[nans_index] = 0

# ��������� ��� ������ � ������� mystery �� int32
mystery_int = np.int32(mystery)

# ������������ �������� � ������� �� ����������� � ���������
# ��������� � ���������� array
array = np.sort(mystery)

# ��������� � ������ table ���������� ������, ���������� �� ������� array
# � �� ������ ���� 5 ����� � 3 �������. ������ ������� ���������� ������ ����
# �� ��������! ��������, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3), order='F')

#  ��������� � ���������� col ������� 2
col = table[:, 1]
