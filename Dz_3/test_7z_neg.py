from checkers import checkout_negative

folder_out = "/home/user/tst/badarx"
folder_ext = "/home/user/tst/ext"


def test_step1(clear_folders, make_files, make_badarx):
    assert checkout_negative("cd {}; 7z e badarx.7z -o{} -y".format(folder_out, folder_ext), "ERROR"), "Test4 Fail"


def test_step2():
    assert checkout_negative("cd {}; 7z t badarx.7z".format(folder_out), "ERROR"), "Test5 Fail"
