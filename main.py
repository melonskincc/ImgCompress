from tkinter import *
from tkinter.filedialog import *
from PIL import Image

info = {'path': []}


def make_app():
    app = Tk()
    # 标签
    Label(app, text='图片压缩小工具', font=('Hack', 20, 'bold')).pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='Open', command=ui_getdata).pack()
    Button(app, text='compress', command=compress).pack()
    app.geometry('300x400')
    return app


def ui_getdata():
    f_name = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_name
    if info['path']:
        for name in f_name:
            lbox.insert(END, name.split('/')[-1])


def compress():
    for f_path in info['path']:
        # 输出路径
        output = './zip/'
        # 图片的文件名
        name = f_path.split('/')[-1]
        # 打开图片
        # image = Img.open(f_path)
        # 图片另存到output文件夹中，图片质量压缩到60%
        # image.save(output + 'C_' + name, quality=10)
        # 如果是.9图片或者非图片文件不做处理,直接做拷贝
        if not f_path.endswith(".9.png") and (f_path.endswith(".png") or f_path.endswith(".jpg")):
            print(
                "--------------------------------------------------------------------------------------------")
            print("currrent file:" + f_path)
            im = Image.open(f_path)
            origin_size = os.path.getsize(f_path)

            if f_path.endswith(".png"):
                im = im.convert('P')
            im.save(output + 'C_' + name, optimize=True)

            target_file = os.path.join(output, 'C_' + name)
            compress_size = os.path.getsize(target_file)
            print('%.2f' % ((origin_size - compress_size) / origin_size))
        else:
            # if not out_dir or out_dir == fromFile:
            #     continue
            shutil.copy(f_path, os.path.join(output, name))


app = make_app()

mainloop()
import os
import shutil

from PIL import Image


def CompressByPillow(fromFile, out_dir):
    print("do CompressByPillow..")
    try:
        for root, dir, files in os.walk(fromFile):
            print("****************************************************************************************")
            print("root dir:" + root)
            print("dir:" + str(dir))
            for file in files:
                current_file = os.path.join(root, file)
                dirName = os.path.basename(root)
                # 如果没有指定输出路径，则默认覆盖当前文件
                if not out_dir:
                    out_dir = fromFile
                targetDir = os.path.join(out_dir, dirName)
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                # 如果是.9图片或者非图片文件不做处理,直接做拷贝
                if not file.endswith(".9.png") and (file.endswith(".png") or file.endswith(".jpg")):
                    print(
                        "--------------------------------------------------------------------------------------------")
                    print("currrent file:" + current_file)
                    im = Image.open(current_file)
                    origin_size = os.path.getsize(current_file)

                    if file.endswith(".png"):
                        im = im.convert('P')
                    im.save(os.path.join(targetDir, file), optimize=True)

                    target_file = os.path.join(targetDir, file)
                    compress_size = os.path.getsize(target_file)
                    print('%.2f' % ((origin_size - compress_size) / origin_size))
                else:
                    if not out_dir or out_dir == fromFile:
                        continue
                    shutil.copy(current_file, os.path.join(targetDir, file))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    CompressByPillow('./zip', '.')
