from zipfile import ZipExtFile


def zeikomi(kingaku, tax):
    return kingaku + kingaku * tax //100

kakaku = 1980
kekka10 = zeikomi(kakaku, 10)
kekka8 = zeikomi(kakaku, 8)
print(kakaku, '円は税率10%で', kekka10, '円・税率8%で', kekka8, '円')
