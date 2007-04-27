#!/usr/bin/python

import Image, ImageFont, ImageDraw
import cgi
import cgitb; cgitb.enable()
import cStringIO

# courbB08.pil PIL Font file uuencoded
courB08_pil ="""eJztl91rFkcUxp+Zt7vGFYzVtiJKICgYlLRWkaBBVGgDraFGCH5gsQp+QMBqabAVRYJYAlakCkoh
CpYgxaLkIu1NvLBeSAStglpqL6xQAsVe2AuL5u2buH3mzGaYPf9AKWTl8d3nl7MzZ2bnazvea9+9
7+PurFWut5e0Zu+s7VybYfKavP7LK3X/5TlM4Q3/OWbyf1ARD/6mgb2SjwtPhbpnq0iKZ6ahrmCj
wqbxdgamRnHOA69jimN5zvIS8cDcUEeVdYzRAw1FHcJYXgPvG4s6Jlgj7xeEequS3wLeNvGvnrEO
tq+Jt82szT+b86+WHlgS2jHGuHF6YHnog1zaupxqCcy3t4X3rVG9iXhgjW+bsFQ80BaxRDywTrF1
VId6toPaqOI2UlsV20ptV2w7tUuxXVSXYl3UvoIZ9kFFPPBJ6D/HLD3QXbwjyDjI6YHPiz5FXiN7
SQ8cDu/N9/1h3veEOP/Oe6gvQnmuvYYe+NL3qYyNVDxw2seF8XKa+jrKJREPnFdx56l+xfqpS4pd
ogZUeQPU91FcKh64GveBeOCaKu8adUM9e4O6reJuU/cUu0c9VM8+pB6r/B5TI+rZEerPUpyhB/6K
5lsqHniuyntO1VR5Nb5CU86FHqZOsTqqXrF66o2ojlQ8zDwVN4+aX86FHqYpXg9YLeevWRzPc7LF
ZG+V1wN6mKXxvMzH6GFaJua5zGNLD7MqmtNcc+hh1oT1oCb5cf6aNj92mbPMGXqY9jCPasLaqQ1h
jMv8pYfZpOI2UR9GcYl4mB1RnMtvB9me8N583B5qb3mNoIf5NGJc1+hhPvPrrjybioc5op49Qh0L
dfj8jlHHQ3s9O059Fc3zRDzMmVKcpYfpU+3oI/umxJyH+TYqLxUPc0X13xVqMMovFQ8zpPIbon6M
WCoeZljVMUz9VIqz9DAP1Dt6QP0a9gpZ7+lhHhXjysreaOhhfiv1vaGH+T2Mv5rbU+hh/uAaOnlN
Xv+Hy4/7mtv3OW5hnpTODIYe5mm0xqbiYf4OcbLv08NU1ZyuuqKLOEvm6sjhJkd8TjRustgkrO3u
vFGjh60r1uyiPHrY6eH84tb7l/SwM8vrAT3snHgNY9wcsoby+Y8edn5UxxTxsIuitrlcFpG9GcVx
/6CHXRrKk72MHrYl3stYB/ceu7I4X02wlWSrCmaF1ehhV7NrovWKHrattI4betj20Fc8r7E87kf2
g+gcy32BHnZDfKZmHPco2xnl4vqlk2yz6r/N1EfRPpiKh90d7VGpeNi9inGPst2lNdbSwx4McS8k
7iDVE/Ytz3qoXsV6qZOKnaTOBDYqjPuRPRfOkz7uHNUf4uQMQg/7XekMYulhB6JnE/GwP0T1JuJh
ryrGM6G9HuWSiIcdDnPmhTs70sPeCuPes1vUXcXuUvcDGxV2n/olOisn4mEfhfOVby/3KDsSlZeI
h32iGOe0faoY57R9ptgzajTKJREPOx7aJnOfHhUbxov0Mz0qU8v50aMyo/wu6VGZrdhsqqH8fnll
HEEz4zj6DNMxK+4X+gyv8cszyoU+4zfmjNAO9zuXrNGXF1gj2ULFFpI1K9ZMtiww//22jGwFXg39
535XkK0O+cl5gz7Du6iP5wd9hvfDs9LP9BnWR/U6tp6sU7FOsi1RLo5tIdsWled+t5HtVO3YSdal
WBfZftW2/WQHVH4HyA6F9+GfPUR2VOV3lKxXsV6yE4qdIDul2Cmys6ptZ8n6Qi7+m7OP7ELoU/8t
dIHsoo8L+V0ku6xyvkw2qNgg2VBgvg+GyK6XyrP0GW5ydE3EuXd5k+xOeOdVibtD9jNm/Qv15O4i"""

# courbB08.pbm font file uuencoded
courB08_pbm ="""eJxNkntM01cUx8+P2/1apUAZEpECq4KRjKhF0E55FYEp4yG6mglz2Q8Q1BhERhhls/zKI+CID4wb
IAPKpk4GAzqZPKKMX2GIUwGJG+ImtKwKjIzXcGuBtncV0Hn+uLnn5Nzv55xv7mdRkbusVjquBACr
0N3B+wCQi/m+ijAf4LGl/wgAiwkNDpRIyyABSjGkBQ/fa3c1bfLs4U8ulDcYUs/502rTpIlO9pyc
Kp/Buql6f3rmZ1NqvpO2SZXf0duY3j0563zjoZpW8AvHRmVeZ/Co36mFR8bERzlsxOMJ+oJshsS5
7rlfzFzmnZFEFnIEZjTGizgLsLzjl4QtrNprBRu10e+u9GgePHjG63bPDw/H87uix0Vtsvkqg9qO
lUimPLiOM4z69YfqIu5Pa2Sr/io6n9Xmf9e+57W1Iapo4lLQBdLSWc/z3KOSlgznDXTW/Flh21kX
IeUIX8FZVL9dwP4NBH5jglYxkBNFmWgMcfsAxM/9gEL5TTwYpnfElR8qQ+WiCgeTHOAfb2bW/cQC
/FozFOOQzAebtjRvQLI7HBtXvaZe25a3Q/1vZpPa+kd1XXKuflr5Cm48YUsUcjMXjsm/sf+22s6z
QAbGZ8mEXMzSE4y9AHhRpltwB1N9ynz5H2MOi0MEi4E5O1ov9ogrFU5cMWAcdgQb3xHFtFK+0pkh
VnYWxltx92j69p6jJ9OnHr+Cq5x5X6Mz70JcX2tEG5LIShM4EHIGoLIRsHzcvEuGwMYA4DZPn7gP
MA1QIgltnt82cTu7j5n76mmz3TU5Bh3PFRTHku52aBgaTnJD7m1c0a3hNjbWWjBtMsP/OFac/LYA
NAAWepdYodB58NBFIuOjNSQ4cgXplqP2RyOe8fd999T8weqBRwLwNFdQobHgA1/YTV8PH+TwV59v
Bo7Y1J4rmHFv3T9e8rmmXdGSuPpSbBnhYJ7V8ICz6AfGcdTpRkpCUU8WcOT8wb+dSHIb6QZapx0M
Y2DO4i7jYV2AUNkkErpQFHVYmFRmYD7OJhDyQSiow4IkrS3TbpQqFA9slE4jnj6peXMTC+N8buJ2
0Uv5eOothuGIiluyCDtff3miBzJHjncOIC3bPT8FLabRPd0TCWy346Mmn9Rz23WyNMJcsnqhQani
3CMFOZuYU7c20zTNVqNbGPNxALWnybeLEcTvXWpc10leI5ae/CI9qBqI686cnO6P6F33e2vAp0nz
9+hnbNeueh/261UJK5aVeSf73ZSXA7dOBXvkXODEb9hVww4KtPNAbPvaZbi0q9kICCl+CiBJSzLv
a8TlntYlC4UHvCRTlaXOy13VAbN0eae2v3hNesWXLsWPkjfOPq7e6zd1fOfc1TckDaylrvleinnT
8Ui87ScLMVhhEx7SUJ8U2zKrRR2Z1dEqZlkr7kDTuhFjpkvse9ZXN0R9H+DlYA4TXVm6/kXDQMyT
eGnJFXlLlSgva5iLUEcbiyDzNqf4Wr9kKYVUIcY40DrnsW4E4zW9QxnHVYx+bo64mIskDWjZgCrq
eVQFrS7Sh/uFLftIidKWbgj6Oq652d4c3v88Dw2JDK7bSWX/ByuaLZI="""

char2numA = {" ":0,"!":1,"\"":2,"#":3,"$":4,"%":5,"&":6,"'":7,"(":8,")":9,"*":10,\
    "+":11,",":12,"-":13,".":14,"/":15,"0":16,"1":17,"2":18,"3":19,"4":20,\
    "5":21,"6":22,"7":23,"8":24,"9":25,":":26,";":27,"<":28,"=":29,">":30,\
    "?":31,"@":32,"A":33,"B":34,"C":35,"D":36,"E":37,"F":38,"G":39,"H":40,\
    "I":41,"J":42,"K":43,"L":44,"M":45,"N":46,"O":47,"P":48,"Q":49,"R":50,\
    "S":51,"T":52,"U":53,"V":54,"W":55,"X":56,"Y":57,"Z":58,"[":59,"\\":60,\
    "]":61,"^":62,"_":63,"^@ NUL":64,"^A SOH":65,"^B STX":66,"^C ETX":67,"^D EOT":68,"^E ENQ":69,"^F ACK":70,\
    "\a":71,"\b":72,"\t":73,"\n":74,"\v":75,"\f":76,"\r":77,"^N SO":78,"^O SI":79,"^P DLE":80,\
    "^Q DC1":81,"^R DC2":82,"^S DC3":83,"^T DC4":84,"^U NAK":85,"^V SYN":86,"^W ETB":87,"^X CAN":88,"^Y EM":89,"^Z SUB":90,\
    "^[ ESC":91,"^\ FS":92,"^] GS":93,"^^ RS":94,"^_ US":95,"FNC3":96,"FNC2":97,"SHIFTB":98,"CODEC":99,"CODEB":100,\
    "FNC4":101,"FNC1":102,"STARTA":103,"STARTB":104, "STARTC":105}

char2numB = {" ":0,"!":1,"\"":2,"#":3,"$":4,"%":5,"&":6,"'":7,"(":8,")":9,"*":10,\
    "+":11,",":12,"-":13,".":14,"/":15,"0":16,"1":17,"2":18,"3":19,"4":20,\
    "5":21,"6":22,"7":23,"8":24,"9":25,":":26,";":27,"<":28,"=":29,">":30,\
    "?":31,"@":32,"A":33,"B":34,"C":35,"D":36,"E":37,"F":38,"G":39,"H":40,\
    "I":41,"J":42,"K":43,"L":44,"M":45,"N":46,"O":47,"P":48,"Q":49,"R":50,\
    "S":51,"T":52,"U":53,"V":54,"W":55,"X":56,"Y":57,"Z":58,"[":59,"\\":60,\
    "]":61,"^":62,"_":63,"`":64,"a":65,"b":66,"c":67,"d":68,"e":69,"f":70,\
    "g":71,"h":72,"i":73,"j":74,"k":75,"l":76,"m":77,"n":78,"o":79,"p":80,\
    "q":81,"r":82,"s":83,"t":84,"u":85,"v":86,"w":87,"x":88,"y":89,"z":90,\
    "{":91,"|":92,"}":93,"~":94,"^? DEL":95,"FNC3":96,"FNC2":97,"SHIFTA":98,"CODEC":99,"FNC4":100,\
    "CODEA":101,"FNC1":102,"STARTA":103,"STARTB":104, "STARTC":105}

char2numC = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,\
    "10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,\
    "20":20,"21":21,"22":22,"23":23,"24":24,"25":25,"26":26,"27":27,"28":28,"29":29,\
    "30":30,"31":31,"32":32,"33":33,"34":34,"35":35,"36":36,"37":37,"38":38,"39":39,\
    "40":40,"41":41,"42":42,"43":43,"44":44,"45":45,"46":46,"47":47,"48":48,"49":49,\
    "50":50,"51":51,"52":52,"53":53,"54":54,"55":55,"56":56,"57":57,"58":58,"59":59,\
    "60":60,"61":61,"62":62,"63":63,"64":64,"65":65,"66":66,"67":67,"68":68,"69":69,\
    "70":70,"71":71,"72":72,"73":73,"74":74,"75":75,"76":76,"77":77,"78":78,"79":79,\
    "80":80,"81":81,"82":82,"83":83,"84":84,"85":85,"86":86,"87":87,"88":88,"89":89,\
    "90":90,"91":91,"92":92,"93":93,"94":94,"95":95,"96":96,"97":97,"98":98,"99":99,\
    "CODEB":100,"CODEA":101,"FNC1":102,"STARTA":103,"STARTB":104, "STARTC":105}
"""
num2char = {0:" ",1:"!",2:"\"",3:"#",4:"$",5:"%",6:"&",7:"'",8:"(",9:")",10:"*",\
    11:"+",12:",",13:"-",14:".",15:"/",16:"0",17:"1",18:"2",19:"3",20:"4",\
    21:"5",22:"6",23:"7",24:"8",25:"9",26:":",27:";",28:"<",29:"=",30:">",\
    31:"?",32:"@",33:"A",34:"B",35:"C",36:"D",37:"E",38:"F",39:"G",40:"H",\
    41:"I",42:"J",43:"K",44:"L",45:"M",46:"N",47:"O",48:"P",49:"Q",50:"R",\
    51:"S",52:"T",53:"U",54:"V",55:"W",56:"X",57:"Y",58:"Z",59:"[",60:"\\",\
    61:"]",62:"^",63:"_",64:"`",65:"a",66:"b",67:"c",68:"d",69:"e",70:"f",\
    71:"g",72:"h",73:"i",74:"j",75:"k",76:"l",77:"m",78:"n",79:"o",80:"p",\
    81:"q",82:"r",83:"s",84:"t",85:"u",86:"v",87:"w",88:"x",89:"Y",90:"z",\
    91:"{",92:"|",93:"}",94:"~",95:"^? DEL",96:"FNC3",97:"FNC2",98:"SHIFTA",99:"CODEC",100:"FNC4",\
    101:"CODEA",102:"FNC1",103:"STARTA",104:"STARTB"}
"""
num2code = {0:[2, -1, 2, -2, 2, -2],1:[2, -2, 2, -1, 2, -2],2:[2, -2, 2, -2, 2, -1],\
    3:[1, -2, 1, -2, 2, -3],4:[1, -2, 1, -3, 2, -2],5:[1, -3, 1, -2, 2, -2],\
    6:[1, -2, 2, -2, 1 -3],7:[1, -2, 2, -3, 1, -2],8:[1, -3, 2, -2, 1, -2],\
    9:[2, -2, 1, -2, 1, -3],10:[2, -2, 1, -3, 1, -2],11:[2, -3, 1, -2, 1, -2],\
    12:[1, -1, 2, -2, 3, -2],13:[1, -2, 2, -1, 3, -2],14:[1, -2, 2, -2, 3, -1],\
    15:[1, -1, 3, -2, 2, -2],16:[1, -2, 3, -1, 2, -2],17:[1, -2, 3, -2, 2, -1],\
    18:[2, -2, 3, -2, 1, -1],19:[2, -2, 1, -1, 3, -2],20:[2, -2, 1, -2, 3, -1],\
    21:[2, -1, 3, -2, 1, -2],22:[2, -2, 3, -1, 1, -2],23:[3, -1, 2, -1, 3, -1],\
    24:[3, -1, 1, -2, 2, -2],25:[3, -2, 1, -1, 2, -2],26:[3, -2, 1, -2, 2, -1],\
    27:[3, -1, 2, -2, 1, -2],28:[3, -2, 2, -1, 1, -2],29:[3, -2, 2, -2, 1, -1],\
    30:[2, -1, 2, -1, 2, -3],31:[2, -1, 2, -3, 2, -1],32:[2, -3, 2, -1, 2, -1],\
    33:[1, -1, 1, -3, 2, -3],34:[1, -3, 1, -1, 2, -3],35:[1, -3, 1, -3, 2, -1],\
    36:[1, -1, 2, -3, 1, -3],37:[1, -3, 2, -1, 1, -3],38:[1, -3, 2, -3, 1, -1],\
    39:[2, -1, 1, -3, 1, -3],40:[2, -3, 1, -1, 1, -3],41:[2, -3, 1, -3, 1, -1],\
    42:[1, -1, 2, -1, 3, -3],43:[1, -1, 2, -3, 3, -1],44:[1, -3, 2, -1, 3, -1],\
    45:[1, -1, 3, -1, 2, -3],46:[1, -1, 3, -3, 2, -1],47:[1, -3, 3, -1, 2, -1],\
    48:[3, -1, 3, -1, 2, -1],49:[2, -1, 1, -3, 3, -1],50:[2, -3, 1, -1, 3, -1],\
    51:[2, -1, 3, -1, 1, -3],52:[2, -1, 3, -3, 1, -1],53:[2, -1, 3, -1, 3, -1],\
    54:[3, -1, 1, -1, 2, -3],55:[3, -1, 1, -3, 2, -1],56:[3, -3, 1, -1, 2, -1],\
    57:[3, -1, 2, -1, 1, -3],58:[3, -1, 2, -3, 1, -1],59:[3, -3, 2, -1, 1, -1],\
    60:[3, -1, 4, -1, 1, -1],61:[2, -2, 1, -4, 1, -1],62:[4, -3, 1, -1, 1, -1],\
    63:[1, -1, 1, -2, 2, -4],64:[1, -1, 1, -4, 2, -2],65:[1, -2, 1, -1, 2, -4],\
    66:[1, -2, 1, -4, 2, -1],67:[1, -4, 1, -1, 2, -2],68:[1, -4, 1, -2, 2, -1],\
    69:[1, -1, 2, -2, 1, -4],70:[1, -1, 2, -4, 1, -2],71:[1, -2, 2, -1, 1, -4],\
    72:[1, -2, 2, -4, 1, -1],73:[1, -4, 2, -1, 1, -2],74:[1, -4, 2, -2, 1, -1],\
    75:[2, -4, 1, -2, 1, -1],76:[2, -2, 1, -1, 1, -4],77:[4, -1, 3, -1, 1, -1],\
    78:[2, -4, 1, -1, 1, -2],79:[1, -3, 4, -1, 1, -1],80:[1, -1, 1, -2, 4, -2],\
    81:[1, -2, 1, -1, 4, -2],82:[1, -2, 1, -2, 4, -1],83:[1, -1, 4, -2, 1, -2],\
    84:[1, -2, 4, -1, 1, -2],85:[1, -2, 4, -2, 1, -1],86:[4, -1, 1, -2, 1, -2],\
    87:[4, -2, 1, -1, 1, -2],88:[4, -2, 1, -2, 1, -1],89:[2, -1, 2, -1, 4, -1],\
    90:[2, -1, 4, -1, 2, -1],91:[4, -1, 2, -1, 2, -1],92:[1, -1, 1, -1, 4, -3],\
    93:[1, -1, 1, -3, 4, -1],94:[1, -3, 1, -1, 4, -1],95:[1, -1, 4, -1, 1, -3],\
    96:[1, -1, 4, -3, 1, -1],97:[4, -1, 1, -1, 1, -3],98:[4, -1, 1, -3, 1, -1],\
    99:[1, -1, 3, -1, 4, -1],100:[1, -1, 4 -1, 3, -1],101:[3, -1, 1, -1, 4, -1],\
    102:[4, -1, 1, -1, 3, -1],103:[2, -1, 1, -4, 1, -2],104:[2, -1, 1, -2, 1, -4],\
    105:[2, -1, 1, -2, 3, -2]}

# input string, output number for checksum
def CheckSum(text,codetype):
    if codetype == "A":
        cs = 103
    if codetype == "B":
        cs = 104
    if codetype == "C":
        cs = 105
    t = 0
    while t < len(text):
        if codetype == "A":
            c = char2numA[text[t]]
        if codetype == "B":
            c = char2numB[text[t]]
        if codetype == "C":
            c = char2numC[text[t]]   
        t = t + 1
        cs = cs + (t * c) 
    cs = cs % 103
    return cs

def BarCodeSize(text):
    cs = ((len(text) + 2) * 11) + 13
    return cs

def BarCodeList(text,codetype):
    if codetype == "A":
        bcl = num2code[103]
    if codetype == "B":
        bcl = num2code[104]
    if codetype == "C":
        bcl = num2code[105]
    stop = [2, -3, 3, -1, 1, -1, 2]
    t = 0
    while t < len(text):
        if codetype == "A":
             bcl.extend(num2code[char2numA[text[t]]])
        if codetype == "B":
             bcl.extend(num2code[char2numB[text[t]]])
        if codetype == "C":
            bcl.extend(num2code[char2numC[text[t]]])
        t = t + 1
    bcl.extend(num2code[CheckSum(text,codetype)])
    bcl.extend(stop)
    return bcl

def BarCodeGen(filename,text,codetype):
    X,Y = BarCodeSize(text)+6,60
    img = Image.new("1", (X,Y), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    decodeFontFile(courB08_pil ,"courB08.pil")
    decodeFontFile(courB08_pbm ,"courB08.pbm")
    font = ImageFont.load("courB08.pil")
    cs = CheckSum(text,codetype)
    
    x = 3
    numlst = BarCodeList(text,codetype)
    for i in numlst:
        if i == 1:
            draw.rectangle((x,0,x+1,49), fill="#000000")
            x = x + 1
        if i == -1:
            draw.rectangle((x,0,x+1,49), fill="#FFFFFF")
            x = x + 1
        if i == 2:
            draw.rectangle((x,0,x+2,49), fill="#000000")
            x = x + 2
        if i == -2:
            draw.rectangle((x,0,x+2,49), fill="#FFFFFF")
            x = x + 2
        if i == 3:
            draw.rectangle((x,0,x+3,49), fill="#000000")
            x = x + 3
        if i == -3:
            draw.rectangle((x,0,x+3,49), fill="#FFFFFF")
            x = x + 3
        if i == 4:
            draw.rectangle((x,0,x+4,49), fill="#000000")
            x = x + 4
        if i == -4:
            draw.rectangle((x,0,x+4,49), fill="#FFFFFF")
            x = x + 4
    ts = (X -(len(text)*6))/2
    draw.text((ts,50),text,font=font, fill=0)
    
    if filename:
    		img.save(filename, "PNG")
    else:
    		#write to file object
    		f = cStringIO.StringIO()
    		img.save(f, "PNG")
    		f.seek(0)
    		
    		#output to browser
    		print "Content-type: image/png\n"
    		print f.read()
    		
def HalfBarCodeGen(filename,text,codetype):
    X,Y = BarCodeSize(text)+6,30
    img = Image.new("1", (X,Y), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    decodeFontFile(courB08_pil ,"courB08.pil")
    decodeFontFile(courB08_pbm ,"courB08.pbm")
    font = ImageFont.load("courB08.pil")
    cs = CheckSum(text,codetype)
    
    x = 3
    numlst = BarCodeList(text,codetype)
    for i in numlst:
        if i == 1:
            draw.rectangle((x,0,x+1,20), fill="#000000")
            x = x + 1
        if i == -1:
            draw.rectangle((x,0,x+1,20), fill="#FFFFFF")
            x = x + 1
        if i == 2:
            draw.rectangle((x,0,x+2,20), fill="#000000")
            x = x + 2
        if i == -2:
            draw.rectangle((x,0,x+2,20), fill="#FFFFFF")
            x = x + 2
        if i == 3:
            draw.rectangle((x,0,x+3,20), fill="#000000")
            x = x + 3
        if i == -3:
            draw.rectangle((x,0,x+3,20), fill="#FFFFFF")
            x = x + 3
        if i == 4:
            draw.rectangle((x,0,x+4,20), fill="#000000")
            x = x + 4
        if i == -4:
            draw.rectangle((x,0,x+4,20), fill="#FFFFFF")
            x = x + 4
    ts = (X -(len(text)*6))/2
    draw.text((ts,21),text,font=font, fill=0)
    #output to file
    
    if filename:
    		img.save(filename, "PNG")
    else:
    		#write to file object
    		f = cStringIO.StringIO()
    		img.save(f, "PNG")
    		f.seek(0)
    		
    		#output to browser
    		print "Content-type: image/png\n"
    		print f.read()
    
def decodeFontFile(data, file):
   """ Decode font file embedded in this script and create file """
   from zlib import decompress
   from base64 import decodestring
   from os.path import exists
   
   # If the font file is missing
   if not exists(file):
      # Write font file
      open (file, "wb").write(decompress(decodestring(data)))
    

#BarCodeGen("out2.png","12340069","B")

form = cgi.FieldStorage()
if form.getvalue("skew"):
	if form.getvalue("ht") == "Full":
		BarCodeGen(None,form.getvalue("skew"),form.getvalue("type"))
	else:
		HalfBarCodeGen(None,form.getvalue("skew"),form.getvalue("type"))
else:
    print "Content-Type: text/html\n\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
    print "\t<TITLE>Output</TITLE>\n"
    print "</HEAD>\n"
    print "<body>"
    print "<h1>Error!  Bar Code form was blank!</h1>"
    print "</body>"
    print "</HTML>\n"