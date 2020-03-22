GRAPH: list = [None, None, None, None, None, None]
IMG: list = [False, False, False, False, False, False]

POSITION_FOR_ANALYSIS = dict.fromkeys([1, 2, 3, 4, 5, 6])

PATH_IMG_TEMP_1 = 'temporary/1.jpg'
PATH_IMG_TEMP_2 = 'temporary/2.jpg'
PATH_IMG_TEMP_3 = 'temporary/3.jpg'
PATH_IMG_TEMP_4 = 'temporary/4.jpg'
PATH_IMG_TEMP_5 = 'temporary/5.jpg'
PATH_IMG_TEMP_6 = 'temporary/6.jpg'


def GET_LIST_ANALYSIS() -> list:
    list_analysis:list = []

    for k,v in POSITION_FOR_ANALYSIS.items():
        if v is not None:
            list_analysis.append(str(k))

    return list_analysis


def add_IMG(number_img: int) -> None:
    IMG[number_img] = True


def del_IMG(number_img: int) -> None:
    IMG[number_img] = False


