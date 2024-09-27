from flet import *
from flet_core.canvas import *



def builder(datax, datay, df)-> Canvas:
    descarte:tuple = ("Sillaginopsis panijus", "Setipinna taty", "Puntius lateristriga", "Polynemus paradiseus", "Pethia conchonius", "Otolithoides pama", "Otolithoides biauritus", "Coilia dussumieri", "Anabas testudineus")
    y:dict = {key: i for i, key in enumerate(descarte)}
    colors_tuple: tuple = (colors.RED, colors.PURPLE,colors.YELLOW, colors.GREEN,colors.ORANGE)
    for i , key in enumerate(y):
        y[key] = (i-1) * (675/len(y))+(675/len(y))

    stroke_paint = Paint(stroke_width=2, style=PaintingStyle.STROKE)
    soft_paint = Paint(stroke_width=1, style=PaintingStyle.STROKE)
    canva = Canvas(
        width= 1250,
        height= 800,
        expand= True,
        shapes= [
            Path(
                [
                    Path.MoveTo(200,0),
                    Path.LineTo(200,750),
                    Path.LineTo(1100,750),
                ],
                paint= stroke_paint
            ),
            Text(1110,330,"X: Peso",TextStyle(size=30)),
            Text(1110,370,"Y: Especie",TextStyle(size=30)),

        ]
    )
    for i in range(0,10):
        canva.shapes.append(
            Path(
                [
                    Path.MoveTo((i+1)*90+200,0),
                    Path.LineTo((i+1)*90+200,750),
                    Path.MoveTo(200,i*75),
                    Path.LineTo(1100,i*75),
                ],
                paint= soft_paint,
            )
        )
    for i in range(len(y)):
        canva.shapes.append(
            Text(10,i * (675/len(y))+(675/len(y)), list(y)[i])
        )
    for i in range(10):
        canva.shapes.append(
            Text(i*90 + 230,770, round(i * ((datax[1]-datax[0])/10)+ datax[0],2))
        )
    
    for i, row in df.iterrows():
        if i ==0:
            continue
        numberMinus = row.iloc[2] - datax[0]
        distance = datax[1] - datax[0]
        x = int(870*numberMinus/distance+205)

        canva.shapes.append(
            Text(x,y[row.iloc[0]],".",TextStyle(size=90, color= colors_tuple[row.iloc[4]]))
        )
    
    return canva
