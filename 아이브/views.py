from django.shortcuts import render

# Create your views here.
def show_원영(request):
    context2 = {
        'name': '장원영',
        'img_src': 'https://mblogthumb-phinf.pstatic.net/MjAxODA3MDVfMjM1/MDAxNTMwNzU4NjYxNzA1.KDcvUPMlED41ZER4ZGRV1oYvwr1TufRbbLF8-sX0L6Qg.WTPZWtIXYRIxHqzy_UMgK4OAY_T09FOu_gpfL34ud5Yg.JPEG.maryjane1440/%EC%9E%A5%EC%9B%90%EC%98%81%ED%99%94%EA%B5%9010.jpg?type=w800',
    }
    return render(request, '아이브/멤버.html', context=context2)


def show_유진(request):
    context = {
        'name': '안유진',
        'img_src': 'https://images.chosun.com/resizer/YBJxk0eHbQR5Mf2kmk77ZcGoX6w=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/P3MGUEUTVCYOOCYSVXVPL6I66A.jpg',
    }
    return render(request, '아이브/멤버.html', context=context)