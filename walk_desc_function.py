import os

def walk_desc(path=None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("������� ����������", root)
        print("---")

        if dirs:
            print("������ �����", dirs)
        else:
            print("����� ���")
        print("---")

        if files:
            print("������ ������", files)
        else:
            print("������ ���")
        print("---")

        if files and dirs:
            print("��� ����:")
        for f in files:
            print("���� ", os.path.join(root, f))
        for d in dirs:
            print("����� ", os.path.join(root, d))
        print("===")

walk_desc()
