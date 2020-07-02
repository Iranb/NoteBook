import os
import threading
def SaveVideo(fileInputPath, outName):
    fpsize = os.path.getsize(fileInputPath) / 1024
    if fpsize >= 150.0: #大于150KB的视频需要压缩
        if outName:
            compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(fileInputPath,outName)
            isRun = os.system(compress)
        else:
            compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(fileInputPath, fileInputPath)
            isRun = os.system(compress)
        if isRun != 0:
            return (isRun,"没有安装ffmpeg")
        return True
    else:
        return True

def Compress_Video(function_name):
    # 异步保存打开下面的代码，注释同步保存的代码
    thr = threading.Thread(target=function_name, args=('../01.avi', '../01_cpd.avi'))
    thr.start()
    #下面为同步代码
    # fpsize = os.path.getsize(self.fileInputPath) / 1024
    # if fpsize >= 150.0:  # 大于150KB的视频需要压缩
    #     compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(
    #         self.fileInputPath, self.fileOutPath)
    #     isRun = os.system(compress)
    #     if isRun != 0:
    #         return (isRun, "没有安装ffmpeg")
    #     return True
    # else:
    #     return True

if __name__ == "__main__":
    Compress_Video(SaveVideo)