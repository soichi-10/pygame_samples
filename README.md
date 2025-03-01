# pygame_samples演習
### ステップ2

#### demo_01.py
ウィンドウサイズ
>~~~
>screen = pygame.display.set_mode([640, 480])
>~~~

ウィンドウの名前
>~~~
>pygame.display.set_caption("pygame demo - window title here")
>~~~

ウィンドウの背景の色
>~~~
>screen.fill((238, 238, 170))
>~~~

図形の種類、色、座標、大きさ
>~~~
>pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
>pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
>pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
>pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))
>~~~

動く点のon,offそれぞれの色
>~~~
>color_on = (240, 120, 120)
>color_off = (120, 120, 120)
>~~~

動く点の四角の横の数
>~~~
>for x0 in range(5):
>~~~

動く点の四角の縦の数
>~~~
>for y0 in range(7):
>~~~

### ステップ3
#### demo_01.py
>x座標を1ずつ増やす
>>~~~
>>x1 += 1
>>~~~
>もしx座標が4ならx座標を0にしてy座標を1増やす
>>~~~
>>if x1 > 4:
>>    x1 = 0
>>    y1 += 1
>>~~~
>もしy座標が6ならy座標を0にする
>>~~~
>>if y1 > 6:
>>    y1 = 0
>>~~~
>
>
>https://github.com/user-attachments/assets/f54b113f-3504-48f6-ab05-73635783311e
>
>
### ステップ4
#### demo_LCD_font_01.py lcd_font_pg.py
0~9を表示させる
>lcd_font_pg.pyに自分のドットマトリックスをかく。
>>~~~
>>LCD_3 = (0, 1, 1, 1, 0,
>>         1, 0, 0, 0, 1,
>>         0, 0, 0, 0, 1,
>>         0, 1, 1, 1, 0,
>>         0, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 1, 1, 1, 0)
>>
>>LCD_4 = (0, 0, 0, 1, 0,
>>         0, 0, 1, 0, 0,
>>         0, 1, 0, 1, 0,
>>         1, 0, 0, 1, 0,
>>         1, 1, 1, 1, 1,
>>         0, 0, 0, 1, 0,
>>         0, 0, 0, 1, 0)
>>
>>LCD_5 = (1, 1, 1, 1, 1,
>>         1, 0, 0, 0, 0,
>>         1, 0, 0, 0, 0,
>>         1, 1, 1, 1, 0,
>>         0, 0, 0, 0, 1,
>>         0, 0, 0, 0, 1,
>>         1, 1, 1, 1, 0)
>>
>>LCD_6 = (0, 0, 1, 0, 0,
>>         0, 1, 0, 0, 0,
>>         1, 0, 0, 0, 0,
>>         1, 1, 1, 1, 0,
>>         1, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 1, 1, 1, 0)
>>
>>LCD_7 = (1, 1, 1, 1, 1,
>>         1, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 0, 0, 1, 0,
>>         0, 0, 1, 0, 0,
>>         0, 0, 1, 0, 0,
>>         0, 1, 0, 0, 0)
>>
>>LCD_8 = (0, 1, 1, 1, 0,
>>         1, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 1, 1, 1, 0,
>>         1, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 1, 1, 1, 0)
>>
>>LCD_9 = (0, 1, 1, 1, 0,
>>         1, 0, 0, 0, 1,
>>         1, 0, 0, 0, 1,
>>         0, 1, 1, 1, 1,
>>         0, 0, 0, 0, 1,
>>         0, 0, 0, 1, 0,
>>         0, 0, 1, 0, 0)
>>
>>LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9)
>>~~~
>
>demo_LCD_font_01.pyで何の数字を表示するか決める
>>~~~
>>code = int((x / 8) % 10)
>>~~~
>
>https://github.com/user-attachments/assets/6ba812dd-0b4c-4e75-81f8-5c428dd3b57c

複数の数字を表示できるようにする
>codeとlcd1.update_colを増やす
>>~~~
>>code = int((x / 8) % 10)
>>code1 = int((x / 10 / 8) % 10)
>>code2 = int((x / 100 / 8) % 10)
>>lcd1.update_col(col=0, code=code2)
>>lcd1.update_col(col=1, code=code1)
>>lcd1.update_col(col=2, code=code)
>>~~~
>![](images/step4.png)

### ステップ5、ステップ6
#### lcd_font_pg.py demo_03.py
demo_lcd_font.pyからLCDフォント表示の要素を抜き出し、demo_02.pyを複製して作ったdemo_03.pyに取り込む。
>lcd_font_pg.pyと違うところを同じにする
>>~~~
>>display1 = Seven_seg(screen)
>>display2 = Seven_seg(screen)
>>
>>num
>>~~~
>>の部分を
>>~~~
>>display1 = LCD_font(screen)
>>display2 = LCD_font(screen)
>>
>>code
>>~~~
>>にする

時分秒をゲットしている方法を調べ、年月日をゲットする。
>時分秒をゲットしている方法を調べる
>>~~~
>>dt_now.hour
>>~~~
>>などの定義を追っていくとdatetime.pyでげっとしていることがわかる。
>>
>年月日をゲットする
>>datetime.pyの中にあるdt_now.day dt_now.month dt_now.yearを使う。

「ー」のLCDフォントを追加する。
>lcd_font_pg.pyにかく
>>lcd_font_pg.pyに「ー」のコードを書いて、code=11で指定する。

LCDフォントによる時刻、日付表示をおこなう。
>dt_now.secondやdt_now.hourなどを使うようにする
>>~~~
>>display1.update_col(col=0, code=int(str(dt_now.year)[0]))
>>display1.update_col(col=1, code=int(str(dt_now.year)[1]))
>>display1.update_col(col=2, code=int(str(dt_now.year)[2]))
>>display1.update_col(col=3, code=int(str(dt_now.year)[3]))
>>display1.update_col(col=4, code=(ord('-')))
>>display1.update_col(col=5, code=dt_now.month // 10)
>>display1.update_col(col=6, code=int(str(dt_now.month)[0]))
>>display1.update_col(col=7, code=(ord('-')))
>>display1.update_col(col=8, code=int(str(dt_now.day)[0]))
>>display1.update_col(col=9, code=dt_now.day % 10)
>>
>>display2.update_col(col=0, code=dt_now.hour // 10)
>>display2.update_col(col=1, code=dt_now.hour % 10)
>>display2.update_col(col=2, code=10 )
>>display2.update_col(col=3, code=dt_now.minute // 10)
>>display2.update_col(col=4, code=dt_now.minute % 10)
>>display2.update_col(col=5, code=10 )
>>display2.update_col(col=6, code=dt_now.second // 10)
>>display2.update_col(col=7, code=dt_now.second % 10)
>>~~~
>>のように時間などの一桁目、二桁目などを使うようにする

各種パラメーターを変化させ、見え方をアレンジしてみる。
>BLOCK_SIZEやBLOCK_INTV、X_ORGなどの数を変える。
>>BLOCK_SIZEで一ブロックの大きさ、BLOCK_INTVでブロック同士の間隔、X_ORG、Y_ORGで座標を変えることができる。

### ステップ7
#### axis_flat.py demo_04.py kadai_01.py
kadai_01.pyからdemo_04.pyに取り込んだコードを使う
>kadai_01.pyを使うのに必要なファイルを移動する
>>minecraft_remote_itkidsからparam_MCJE.pyやmcjeフォルダをpygame_samplesに移動する
>
>param_MCJE.pyをマイクラリモコンができるように設定してdemo_04.pyを実行する
>>PLAYER_NAME、PLAYER_ORIGIN、ADRS_MCR、PORT_MCRを公開サーバーでリモコンをできるように設定する。
>>demo_04.pyを実行する

axis_flat.pyを動かす