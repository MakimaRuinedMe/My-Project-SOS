@namespace
class SpriteKind:
    Friendly = SpriteKind.create()
    Silly = SpriteKind.create()
    shopkind = SpriteKind.create()
    door = SpriteKind.create()
    npc = SpriteKind.create()
    theothernpc = SpriteKind.create()
    EnemyProjectile = SpriteKind.create()
    umm = SpriteKind.create()
    Ceo = SpriteKind.create()
    sign = SpriteKind.create()
    Bodyguard = SpriteKind.create()
    bodygaurd2 = SpriteKind.create()
def levelset():
    sprites.destroy(house)
    sprites.destroy_all_sprites_of_kind(SpriteKind.theothernpc)

def on_on_overlap(sprite, otherSprite):
    story.sprite_say_text(shop_keeper, "*Old man grunting noises*")
    game.show_long_text("No one visits hardware stores anymore. That's so last century ago! Wow, I'm old... and I can't go adventuring. Not that that's going to matter with the situation we're in.... Wait, I know! You could take this off my hands! Put this to good use, or maybe save our souls with this perhaps? ",
        DialogLayout.BOTTOM)
    story.show_player_choices("Take it", "Refuse")
    if story.check_last_answer("Take it"):
        game.show_long_text("Thanks kiddo! I never got around to using this, but it seems like a powerful item! To use it, PRESS B. Do use it carefully, you can hurt yourself and take recoil DAMAGE from it... Hey! Don't point it at me! Go use it at the PARK or something! Anyway, now that my hands are empty, I can go off and play space golf for the remaining time we have left!",
            DialogLayout.BOTTOM)
    else:
        game.show_long_text("Man, even in my final days, stupid kids are giving me trouble. Scram then!",
            DialogLayout.BOTTOM)
    pause(100)
    game.show_long_text("Makes me wish we didn't take the sun for granted... It all started with the phones, man... Also, I have my suspicions it has to do with that Future Organization, but people just dismiss me as a senile old man... Whatever, at least people leave me alone!",
        DialogLayout.BOTTOM)
    pause(10000)
sprites.on_overlap(SpriteKind.Friendly, SpriteKind.player, on_on_overlap)

def on_b_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 1 1 1 . . . . 
                    . . . . . . . . . 1 1 1 1 . . . 
                    . . . . . . . . 1 1 5 1 1 . . . 
                    . . . . . . . . 1 5 5 5 5 1 . . 
                    . . . . . . . 1 5 9 9 5 5 1 . . 
                    9 9 9 9 9 9 9 5 5 9 9 9 5 1 1 1 
                    9 9 9 9 9 9 9 9 9 9 9 9 5 5 5 1 
                    9 9 9 9 9 9 9 9 9 9 9 9 9 5 5 1 
                    9 9 9 9 9 9 9 5 5 5 9 9 9 5 5 1 
                    . . . . . . . 1 1 5 5 9 5 5 1 1 
                    . . . . . . . . 1 1 5 5 5 1 . . 
                    . . . . . . . . . 1 1 1 1 1 . . 
                    . . . . . . . . . . 1 1 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        playersprite,
        200,
        0)
    if projectile2.overlaps_with(playersprite):
        info.change_life_by(2)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile(sprite2, location):
    global current_level
    current_level += -1
    Change_Level(current_level)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile32
    """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite2):
    game.show_long_text("I'm on my phone right now. Just pass already. ",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.Bodyguard, SpriteKind.player, on_on_overlap2)

def on_on_overlap3(sprite4, otherSprite3):
    sprites.destroy(projectile)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap3)

def on_on_overlap4(sprite5, otherSprite4):
    game.show_long_text("You! Who are you?! Only authorized people are allowed here! Wait, you have our uniform... Are you an intern here or something? Mmmm... Well, don't do anything stupid in front of our CEO! He's here to discuss some Top secret stuff at a conference!",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.umm, SpriteKind.player, on_on_overlap4)

def on_overlap_tile2(sprite6, location2):
    global current_level
    current_level += 1
    Change_Level(current_level)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile39
    """),
    on_overlap_tile2)

def on_on_zero(status):
    sprites.destroy(myEnemy, effects.fire, 500)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def Change_Level(Level_number: number):
    global myEnemy, mySprite5, projectile, projectile2, statusbar, mySprite6, mySprite7, mySprite_8, my_Sprite_9
    if Level_number == 1:
        pass
    elif Level_number == 2:
        myEnemy = sprites.create(assets.image("""
            myImage
        """), SpriteKind.enemy)
        animation.run_image_animation(myEnemy,
            [img("""
                    ..................................................
                                ..................................................
                                ..................................................
                                ....................ffffffff......................
                                ..................ff66666666ff....................
                                .................f699999999999f...................
                                ................f69999999999999f..................
                                ...............f6999999999999999f.................
                                ...............f9999999999999999f.................
                                ..............f6999f999999999f999f................
                                ..............f69966f9999999f6699f................
                                ..............f999966f99999f66999f................
                                .............f69999966fffff6699996f...............
                                .......f.....f6999999fdeeddf999996f...............
                                ......f6f.f..f6999999f12211f999996f...............
                                .......f6f6f.f6999999f12211f999996f...............
                                .......f666f.f69999996fffff6999996f...............
                                ........f66f.f69999999666669999996f....f..........
                                .......f9ff..f699f999999999999f996f...f9f.........
                                ......f9f.....f999ff99999999ff999f.....f9f........
                                .....f9f......f9999ffffffffff9999f......f6f.......
                                ....f69f......f99999f1eeee1ff9999f......f6f.......
                                ....f699f.....f999999ff333ff99999f.....f66f.......
                                .....f699ff..f996999999fff99996699f..ff66f........
                                ......f6999ff9999669999999999669999ff666f.........
                                .......ff699996f99999969999999999999666f..........
                                .........ff666f.f9999666999999999f666ff...........
                                ...........fff..f99966f669999f69f.fff.............
                                ...............f69966fff6999f669f.................
                                ............fff66666ff.ff699f6669ff...............
                                ...........f666666fff...f669fff6669fff............
                                ............fffffff.....ff66f.fff66666f...........
                                .........................ff66f..ffffff............
                                ..........................fff.....................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                """),
                img("""
                    ..................................................
                                ..................................................
                                ..................................................
                                ....................ffffffff......................
                                ..................ff66666666ff....................
                                .................f699999999999f...................
                                ................f69999999999999f..................
                                ...............f6999999999999999f.................
                                ...............f999f999999999f99f.................
                                ..............f69966f9999999f6699f................
                                ..............f699966f99999f66999f................
                                ......f.......f9999966fffff669999f................
                                .....f6f..f..f6999999fddeedf999996f...............
                                ......f6ff6f.f6999999f11221f999996f.....f.........
                                ......f6666f.f6999999f11221f999996f....f9ff.......
                                .......f666f.f6999999f11221f999996f.....f99f......
                                .......f666f.f69999999fffff9999996f.....f99f......
                                ......f9fff..f69999999999999999996f......ff6f.....
                                .....f9f.....f69f99999999999999f96f......ff6f.....
                                ...ff9f.......f99ff1f999999f1ff99f......f666f.....
                                ..f669f.......f999ffffffffffff999f......f666f.....
                                ..f6699f......f9999feeeeeeeef9999f....ff666f......
                                ...ff699fff...f99999feeeeeeef9999f.fff666ff.......
                                ...ff699fff..f9969999f33333f999999f99666f.........
                                .....f69999ff9999999999fff99996699999666f.........
                                ......ff6699996f9669999999999669999666ff..........
                                ........fff666ff99966f6669999f69ffffff............
                                ...........fff.f99966f6669999f69f.................
                                ...............f99966f6669999f69f.................
                                ...............f99966f6669999f69f.................
                                ...............f69966fff6999f669f.................
                                .............ff66666ff.ff699f6669ff...............
                                ............ff6666fff...f669fff6669fff............
                                ...........f666ffff.....ff66f.fff66666f...........
                                ...........f6ff..........ff66f..ffffff............
                                ...........f6f............fff.....................
                                ............f.....................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                                ..................................................
                """)],
            300,
            True)
        mySprite5 = sprites.create(img("""
                . . . . . 8 8 8 8 8 . . . . . . 
                            . . . . 8 8 8 8 8 8 8 . . . . . 
                            . . . . 8 8 e 8 e 8 8 . . . . . 
                            . . . 8 8 b f e f b 8 8 . . . . 
                            . . . 8 8 1 f e f 1 8 8 . . . . 
                            . . . 8 8 3 e e e 3 8 8 . . . . 
                            . . . . 8 c e 2 e c 8 . . . . . 
                            . . . . c a a d a a c . . . . . 
                            . . . c a a a a a a a c . . . . 
                            . . . e e a a a a a e e . . . . 
                            . . . e e a a a a a e e . . . . 
                            . . . . . b a a a b . . . . . . 
                            . . . . . b b f b b . . . . . . 
                            . . . . . b b f b b . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.status_bar)
        tiles.place_on_tile(mySprite5, tiles.get_tile_location(13, 11))
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        tiles.place_on_tile(myEnemy, tiles.get_tile_location(6, 5))
        myEnemy.follow(mySprite)
        cancelout()
        sprites.destroy_all_sprites_of_kind(SpriteKind.sign)
    elif Level_number == 3:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        cancelout()
        tiles.place_on_tile(playersprite, tiles.get_tile_location(2, 4))
        tiles.place_on_tile(myEnemy, tiles.get_tile_location(7, 4))
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . e . . . . . . . . . . 
                            . . . . . . e . . . . . . . . . 
                            . . . . e e e . . . . . . . . . 
                            . . . . . e 2 e . . . . . . . . 
                            . . e e . e 2 2 e e . . . . . . 
                            . . . . e 2 2 2 2 2 e . . . . . 
                            . . . . e 2 5 2 2 2 e . . . . . 
                            . . . e 5 2 5 5 4 2 2 e . . . . 
                            . . . e 5 5 1 5 5 4 2 e . . . . 
                            . . . e 4 5 1 1 5 4 2 e . . . . 
                            . . . . e 5 5 1 1 2 e . . . . . 
                            . . . . . e 5 4 2 e . . . . . . 
                            . . . . . . e e e . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            myEnemy,
            50,
            0)
        projectile.follow(playersprite, 30)
        projectile2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 1 1 1 . . . . 
                            . . . . . . . . . 1 1 1 1 . . . 
                            . . . . . . . . 1 1 5 1 1 . . . 
                            . . . . . . . . 1 5 5 5 5 1 . . 
                            . . . . . . . 1 5 9 9 5 5 1 . . 
                            9 9 9 9 9 9 9 5 5 9 9 9 5 1 1 1 
                            9 9 9 9 9 9 9 9 9 9 9 9 5 5 5 1 
                            9 9 9 9 9 9 9 9 9 9 9 9 9 5 5 1 
                            9 9 9 9 9 9 9 5 5 5 9 9 9 5 5 1 
                            . . . . . . . 1 1 5 5 9 5 5 1 1 
                            . . . . . . . . 1 1 5 5 5 1 . . 
                            . . . . . . . . . 1 1 1 1 1 . . 
                            . . . . . . . . . . 1 1 . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            playersprite,
            200,
            0)
        statusbar = statusbars.create(60, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(myEnemy, 0, 0)
        statusbar.set_color(5, 15, 2)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    elif Level_number == 4:
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        cancelout()
        sprites.destroy_all_sprites_of_kind(SpriteKind.status_bar)
        mySprite6 = sprites.create(img("""
                . . . . . f f f f f . . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . . f f e f e f f . . . . . 
                            . . . f f b f d f b f f . . . . 
                            . . . f f 1 f d f 1 f f . . . . 
                            . . . f f 3 d d d 3 f f . . . . 
                            . . . . f c d 2 d c f . . . . . 
                            . . . . c 8 1 f 1 8 c . . . . . 
                            . . . c 8 8 f 1 f 8 8 c . . . . 
                            . . . d d 8 8 8 8 8 d d . . . . 
                            . . . d d f f f f f d d . . . . 
                            . . . . . 8 8 8 8 8 . . . . . . 
                            . . . . . 8 8 f 8 8 . . . . . . 
                            . . . . . 8 8 f 8 8 . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.umm)
        tiles.place_on_tile(mySprite6, tiles.get_tile_location(7, 11))
    elif Level_number == 0:
        pass
    else:
        tiles.set_current_tilemap(tilemap("""
            level17
        """))
        scene.set_background_color(1)
        cancelout()
        mySprite7 = sprites.create(img("""
                . . . . . 5 5 5 5 5 . . . . . . 
                            . . . . 5 5 5 5 5 5 5 . . . . . 
                            . . . 5 5 5 4 5 4 5 5 5 . . . . 
                            . . . 5 f 1 f d f 1 f 5 . . . . 
                            . . . 5 1 1 f f 1 1 f 5 . . . . 
                            . . . 5 f f f d f f f 5 . . . . 
                            . . . . 5 4 d 2 d 4 5 . . . . . 
                            . . . . c f 1 f 1 f c . . . . . 
                            . . . c f f f 1 f f f c . . . . 
                            . . . d d f f f f f d d . . . . 
                            . . . d d f f f f f d d . . . . 
                            . . . . . b b b b b . . . . . . 
                            . . . . . b b f b b . . . . . . 
                            . . . . . b b f b b . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ceo)
        tiles.place_on_tile(mySprite7, tiles.get_tile_location(7, 4))
        sprites.destroy_all_sprites_of_kind(SpriteKind.umm)
        tiles.place_on_tile(playersprite, tiles.get_tile_location(7, 13))
        mySprite_8 = sprites.create(img("""
                . . . . . e e e e e . . . . . . 
                            . . . . e e e e e e e . . . . . 
                            . . . e e e 4 e 4 e e e . . . . 
                            . . . e f 1 f d f 1 f e . . . . 
                            . . . e 1 1 f f 1 1 f e . . . . 
                            . . . e f f f d f f f e . . . . 
                            . . . . e 4 d 2 d 4 e . . . . . 
                            . . . . c 7 1 f 1 7 c . . . . . 
                            . . . c 7 7 7 1 7 7 7 c . . . . 
                            . . . d d 7 7 7 7 7 d d . . . . 
                            . . . d d 7 7 7 7 7 d d . . . . 
                            . . . . . c c c c c . . . . . . 
                            . . . . . c c f c c . . . . . . 
                            . . . . . c c f c c . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Bodyguard)
        tiles.place_on_tile(mySprite_8, tiles.get_tile_location(7, 11))
        my_Sprite_9 = sprites.create(img("""
                . . . . . f f f f f . . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . f f f e f e f f f . . . . 
                            . . . f c 1 c 4 c 1 c f . . . . 
                            . . . f 1 1 c c 1 1 c f . . . . 
                            . . . f c c c 4 c c c f . . . . 
                            . . . . f e 4 2 4 e f . . . . . 
                            . . . . c 8 1 f 1 8 c . . . . . 
                            . . . c 8 8 8 1 8 8 8 c . . . . 
                            . . . 4 4 8 8 8 8 8 4 4 . . . . 
                            . . . 4 4 8 8 8 8 8 4 4 . . . . 
                            . . . . . 6 6 6 6 6 . . . . . . 
                            . . . . . 6 6 f 6 6 . . . . . . 
                            . . . . . 6 6 f 6 6 . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.bodygaurd2)
        tiles.place_on_tile(my_Sprite_9, tiles.get_tile_location(9, 11))
    tiles.place_on_random_tile(playersprite, assets.tile("""
        myTile1
    """))

def on_overlap_tile3(sprite7, location3):
    global current_level
    current_level += 1
    Change_Level(current_level)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile37
    """),
    on_overlap_tile3)

def on_on_overlap5(sprite8, otherSprite5):
    game.show_long_text("Ummm, I think I heard some weird noises coming from the PARK! Man, ever since the sun went missing, things have only been getting weirder from here...",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.npc, SpriteKind.player, on_on_overlap5)

def cancelout():
    sprites.destroy_all_sprites_of_kind(SpriteKind.npc)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy_all_sprites_of_kind(SpriteKind.theothernpc)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Silly)
    sprites.destroy_all_sprites_of_kind(SpriteKind.shopkind)
    sprites.destroy_all_sprites_of_kind(SpriteKind.food)

def on_on_overlap6(sprite9, otherSprite6):
    game.show_long_text("I was looking forward to tanning today... What am I going to do now?! Please save us...",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.theothernpc, SpriteKind.player, on_on_overlap6)

def on_on_overlap7(sprite10, otherSprite7):
    global current_level
    current_level += 1
    Change_Level(current_level)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap7)

def on_overlap_tile4(sprite11, location4):
    global current_level
    current_level += 1
    Change_Level(current_level)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile8
    """),
    on_overlap_tile4)

def on_on_overlap8(sprite12, otherSprite8):
    normal()
sprites.on_overlap(SpriteKind.player, SpriteKind.door, on_on_overlap8)

def on_on_overlap9(sprite13, otherSprite9):
    game.show_long_text("THE PARK", DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.sign, SpriteKind.player, on_on_overlap9)

def on_on_overlap10(sprite14, otherSprite10):
    game.show_long_text("I don't get paid enough to ID people, so just pass. The meeting's starting soon.",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.bodygaurd2, SpriteKind.player, on_on_overlap10)

def on_on_overlap11(sprite15, otherSprite11):
    game.show_long_text("AAAAA!!!! PLEASE SAVE US!! Go up to that hideous creature and kill it! Please!! ",
        DialogLayout.BOTTOM)
    pause(20000)
sprites.on_overlap(SpriteKind.status_bar, SpriteKind.player, on_on_overlap11)

def nothing():
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy(projectile)

def on_on_overlap12(sprite16, otherSprite12):
    global shop_keeper, mySprite
    levelset()
    shop_keeper = sprites.create(img("""
            . . . . . . 4 4 4 4 . . . . . . 
                    . . . . 4 4 d d d d 4 4 . . . . 
                    . . . 4 d d d d d d d d 4 . . . 
                    . . 4 4 d d d d d d d d 4 4 . . 
                    . . 4 1 d d d d d d d 1 1 4 . . 
                    . . 4 1 1 d d d d d d 1 1 4 . . 
                    . . 4 1 1 1 1 1 1 1 1 1 1 4 . . 
                    . . 4 1 1 1 d d d d 1 1 1 4 . . 
                    . . 4 1 1 d d d d d d 1 1 4 . . 
                    . . 4 d d d d d d d d d d 4 . . 
                    . . . 4 d d d d d d d d 4 . . . 
                    . . e 4 f f f f f f f f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.Friendly)
    shop_keeper.set_position(120, 275)
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . e e e e e e e e . . . . 
                    . . . e d d d 4 4 4 4 4 e . . . 
                    . . e d d d d d d d 4 4 4 e . . 
                    . . e d d d d d d d d 4 4 e . . 
                    . . e e e e e e e e e e e e . . 
                    . . e d d d d d d d d d 4 e . . 
                    . . e d d d d d d d d d 4 e . . 
                    . . e e e e e e e e e e e e . . 
                    . . e d d d d d d d d d 4 e . . 
                    . . e d 1 5 d d d d d d 4 e . . 
                    . . e e 1 5 e e e e e e e e . . 
                    . . e d d d d d d d d d 4 e . . 
                    . . e d d d d d d d d d 4 e . . 
                    . . e e e e e e e e e e e e . . 
                    . . e d d d d d d d d d 4 e . .
        """),
        SpriteKind.door)
    mySprite.set_position(120, 0)
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.shopkind)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap12)

def on_on_overlap13(sprite17, otherSprite13):
    game.show_long_text("Someone should check on that old man who lives in the big house... He's very crazed as is, and I bet this situation isn't making it better.... ",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.shopkind, SpriteKind.player, on_on_overlap13)

def normal():
    global mySprite6, mySprite
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.door)
    mySprite6 = sprites.create(img("""
            . . . . . 3 3 3 3 3 . . . . . . 
                    . . . . 3 3 3 3 3 3 3 . . . . . 
                    . . . . 3 3 2 3 2 3 3 . . . . . 
                    . . . 3 3 b f d f b 3 3 . . . . 
                    . . . 3 3 1 f d f 1 3 3 . . . . 
                    . . . 3 3 d d d d d 3 3 . . . . 
                    . . . . 3 f d 2 d f 3 . . . . . 
                    . . . . f b b d b b f . . . . . 
                    . . . f b b b b b b b f . . . . 
                    . . . 4 4 b b b b b 4 4 . . . . 
                    . . . d d b b b b b d d . . . . 
                    . . . . . 2 b b b 2 . . . . . . 
                    . . . . . 2 2 f 2 2 . . . . . . 
                    . . . . . 2 2 f 2 2 . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.shopkind)
    mySprite = sprites.create(img("""
            . . . . . 5 5 5 5 5 . . . . . . 
                    . . . . 5 5 5 5 5 5 5 . . . . . 
                    . . . . 5 5 4 5 4 5 5 . . . . . 
                    . . . 5 5 b f d f b 5 5 . . . . 
                    . . . 5 5 1 f d f 1 5 5 . . . . 
                    . . . 5 5 3 d d d 3 5 5 . . . . 
                    . . . . 5 a d 2 d a 5 . . . . . 
                    . . . . a 3 3 d 3 3 a . . . . . 
                    . . . a 3 3 3 3 3 3 3 a . . . . 
                    . . . 4 4 3 3 3 3 3 4 4 . . . . 
                    . . . d d 3 3 3 3 3 d d . . . . 
                    . . . . . c 3 3 3 c . . . . . . 
                    . . . . . c c f c c . . . . . . 
                    . . . . . c c f c c . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.theothernpc)
    tiles.place_on_tile(mySprite6, tiles.get_tile_location(5, 12))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile27
    """))

def on_on_overlap14(sprite18, otherSprite14):
    game.show_long_text("Just wait... Now that we shrunk the sun and released monsters, people will HAVE to rely on our technology for ages to come! MWAHAHAHA! ... ............. .................... ... wait, you aren't my bodyguard! Shoot! Now you found out about the Top Secret report! You're going to have to be elimin- wait, what weapon is that?! Don't point that at me! STOP-",
        DialogLayout.BOTTOM)
    scene.camera_shake(10, 2000)
    pause(3000)
    game.show_long_text("....You think it's over by killing me? Heh... Be prepared for a lifetime of hardship... We already released more monsters in this world AND someone else higher than me has the SUN in their possession! Unless you start up a team and somehow take them down, THIS is everyone's new reality! Get.. used... to... it... *cough*",
        DialogLayout.BOTTOM)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Ceo)
    game.show_long_text("Woo! You beat the REAL enemy of the game! Congratulations!",
        DialogLayout.BOTTOM)
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
sprites.on_overlap(SpriteKind.Ceo, SpriteKind.player, on_on_overlap14)

def on_on_destroyed(sprite19):
    game.show_long_text("Woo! Thank you for saving us! We thought we were goners! ",
        DialogLayout.BOTTOM)
    pause(100)
    game.show_long_text("Ever since the sun has been gone, these weird creatures have been coming up everywhere! Maybe stop by the FUTURE ORG HEADQUARTERS! They'll probably know what to do!",
        DialogLayout.BOTTOM)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_overlap15(sprite20, otherSprite15):
    sprites.destroy(projectile)
    statusbar.value += -20
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap15)

def on_on_overlap16(sprite21, otherSprite16):
    game.show_long_text("The sun is extremely important in our society! I mean, what kind of Solarpunk city works without a sun?! It wouldn't make sense! Please save us, we're literally doomed if the sun doesn't come back....!",
        DialogLayout.BOTTOM)
    pause(5000)
sprites.on_overlap(SpriteKind.Silly, SpriteKind.player, on_on_overlap16)

my_Sprite_9: Sprite = None
mySprite_8: Sprite = None
mySprite7: Sprite = None
statusbar: StatusBarSprite = None
mySprite5: Sprite = None
myEnemy: Sprite = None
projectile: Sprite = None
projectile2: Sprite = None
shop_keeper: Sprite = None
mySprite6: Sprite = None
mySprite: Sprite = None
house: Sprite = None
playersprite: Sprite = None
current_level = 0
tiles.set_current_tilemap(tilemap("""
    level6
"""))
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffff44444eefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffffffff
        fffff4444444eefffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff5ffffffffffffffffffff111111dfffffffffffffffffffff
        ffff444444444eeffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111dddfffffffffffffffffff
        fff44444444444eefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111ddfffff1ffffffffffff
        fee444444444444efffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111111fffffffffffffffffffffffffffffffffffffff1ffffff111111111111dffffffffffffffffff
        ef4444444444444e5ffffffffffffffffffffffffffffffffffffffffffffffffff111111111111111111111ffffffffffffffffffffffffffffffffffffffff111bcb1111b11ddfffffffffffffffff
        5f4444444444444ef5fffffffffffffffffffffffffffffffffffffffffffffff111111111111111111111111111ffffffffffffffffffffffffffffffffffff1111b11111cb11dfffffffffffffffff
        f5444444444444455ffffffffff1ffffffffffffffff5fffffffffffffffff11111111111111d1111dddddddddd111ffffffffffffffffffffffffffffffffff1111111111b111dfffffffffffffffff
        ff5555444444455efffffffffffffffffffffffffff555fffffffffffff11111111111111111dddddd1111111111111fffffffffffffffffffffffffffffffff11111111111111dfffffffffffffffff
        fff44455555554eeffffffffffffffffffffffffffff5ffffffffffffffdd11111ddd1111111111111111111111111111fffffffffffffffffffffffffffffff11111111111111dfffffffffffffffff
        ffff444444444eefffffffffffffffffffffffffffffffffffffffff7669ddd111111ddddd111111111111111111111111ffffffffffffffffffffffffffffff11111111bcb111dfffffffffffffffff
        fffffe444444eefffffffffffffffffffffffffffffffffffffffff7776699dd111111111dd1111111111111111111111111fffffffffffffff1ffffffffffff11bcb1111b111ddfffffffffffffffff
        ffffffeeeeeeefffffffffffffffffffffffffffffffffffffffff777776699dd111111111dd111111111111111111111111dffffffffffffffffffffffffffff11b111111111dffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff77777777669ddd11111111ddd111111111111111111111dd9fffffffffffffffffffffffffff11111111111ddffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff77777777777669ddd1111111111111dd11111ddddd1111dd999fffffffffffffffffffffffffff11111111dddfffffffffffffffffff
        fffffffffffffffffffffffffffffffffff444fffffffffffff777777777777766699dd1111111111ddddd1dd1111dddddd99999ffffffffffffffffffffffffffff11111ddfffffffffff1fffffffff
        fffffffffffffffffffffffffffffffffff4f4ffffffffffff777777777777777766999dddd11111dd111ddd1111111dd999999967ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff1ffffff1fffffffffffffff444fffffffffff77777777777777777769999999dddd1d111111111111ddd99999996677fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff777777777777777777769999999999ddddddddddddddd999999999967777fffffffffffffffffffffffffffff1ffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff667777777777777777766699999999999999999999999999999999667777ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff7767777777777777777777766669999999999999999999999999999677777ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff77767777777777777777777777669999999999999996999999999996777777ffffffffffff1ffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffff1ffffffffffffffff777776677777777777777777777769999999999999996999999999996777777fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff7777776677777777777777777777699999999999999969999999999967777777ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffff1ffffffffffffffffffffffffffffffffffff77777777666777777777777777666699999999999999966999999999667777777ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff777777777766667777777777766966999999999999999666999999666777777777fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff7777777777777766666677777769999999999999999999666699996777777777777ffffffffffffffffffffff1ffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff77777777777777777666666667699999999999999999999677699966777777777777ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffff1ffffffffffffffffffffffffffffff77777777777777777776699966969999999999999999996677699996667777777777ffffffffffffffffffffffffffffffffeeeffff1ffffffff
        ffffffffffffffffffffffffffffffffff1ffffffff7777777777777777777776999969669999999999999999966666999999667777777777fffffffffffffffffffffffffffeeee22efffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff7777777777777777677776999966669999999999999999999669999999966667777777ffffffffffffffffffffffffeee222222efffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff77777777777777776777769999999999999999999999999999699999999999677777766fffffffffffffffffffffffe22222222efffffffffffff
        ffffffffffffffffffff1fffffffffffffffffffff777777777777777767777769999999999999999999999999999999999999999666666677fffffffff5ffffffffffffd1e222222eefffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff777777777777777667776769999999999999999999999999999999966666666677777777ffffffff555fffffffffffd11ee2222eefffffffffffff
        fffffffffffff5ffffffffffffffffffffffffffff777777777777777677776769999999999999999999999999999996667777667777777777fffffffff5fffffffffffd1c111e22eeefffffffffffff
        ffffffffffff555fffffffffffffffffffffffffff777777777777777677766769999999999999999999999999966666777777777777777777ffffffffffffffffffffd1c9c111eeeeefffffffffffff
        fffffffffffff5ffffffffffffffffffffffffffff677777777777777776667769999999999999999999999999967777777777777777777777fffffffffffffffffffd1c99c111bbdeefffffffffffff
        ffffffffffffffffffffffffffffffff5fffffffff667777777777777777777769999999999999999999999999996677777777777777777777fffffffffffffffffffd1c9c111bbdeeffffffffffffff
        fffffffffffffffffffffffffffffff555ffffffff967776667777777777777769999999999999999999999999999677777777777777777777ffffffffffffffffffd11cc111bbbdffffffffffffffff
        ffffffffffffffffffffffffffffffff5fffffffff966776966777777777777669999999999999999999999999996677677777777777777777fffffffffffffffffd1111111bbbdfffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff996776996677777776777699999999999999999999999999996666666777777777777777ffffff444ffffffff1111111bbbdffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff996776999666777776777699999999999999999999999999999999996666677777777777ffffff4f4ffffffff111111bbbdfffffffffffff1fffff
        ffffffffffffffffffffffffffffffffffffffffff996776999996666676776699999999999999999999999999996666999999666666777666ffffff444fffffff111111bbbdff1fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff996676699999999666676999999999999999999999999999966776999999999999666699fffffffffffffffe11111bbbdfffffffffffffffffffff
        fffff1fffffffffffffffff444ffffffffffffffff999677699999999967776999999999999999999999999999967776999999999999999999ffffffffffffffed1111bbbdffffffffffffffffffffff
        fffffffffffffffffffffff4f4ffffffffffffffff999667669999999967776999999999999999999999999999667766999999999999669999ffffffffffffffe2d11bbddfffffffffffffffffffffff
        fffffffffffffffffffffff444ffffffffffffffff999966969999999967776999999999999999999999999996677669999999999999676669fffffffffffffe222dbddfffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffff1fffffffff999996666999999967776999999999999999999999999999666999999999999999667766fffffffffffffe22effffffffffffffffff444ffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999666699999996776999999999999999999999999999999999996666666669967776fffffffffffffeeefffffffffffffffffff4f4ffffffff
        ffffffffffffffffff1ffffffffffffffffffffffff99999999699999996776999999999999999999999999666666666667777777769966666fffffffffffffffffffffffffffffffffff444ffffffff
        fffffffffffffffffffffffffffffffffffffffffff9999999966999999667699999999999999999999999667777777777777777776699999ffffffffffffff1ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff9999999996999999966699996999999999999999999677777777777777777777699999ffffffffffffff1ffffffffffffffffffffffffffffffff
        ffffffffff5fffffffffffffffffffffffffffffffff999999996999999999999999999999999999999996677777777777777777777699999ffffffffffffff1ffffffffffffffffffffffffffffffff
        fffffffff555fffffffffffffffffffffffff5ffffff99996666669999996666669996999999999999999677777777777777777777766999fffffff1fffff111ffffffffffffffffffffffffffffffff
        ffffffffff5fffffffffffffffffffffffff555ffffff9996777776699996677766999996999999999999677777777777777777777776999fffffffffffff111ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff5fffffff996677777766699966666699969999999999999967777777777777777777777699fffffffffffff1ddfffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff96677777777766699999999999999999999999996677777777777777777777769fffffffffffff11dffffffffffffffffffffffffffff5fffff
        ffffffffffffffffffffffffffffffffffffffffffffff9667777777777666666999969969999999999999667777777777777777777769ffffffffffff1dddfffffffffffffffffffffffffff555ffff
        fffffffffffffffffffffffffffffffffffffffffffffff96777777777777777669999999999999999999996777777777777777777776fffffffffff111dffffffffffffffffffffff1fffffff5fffff
        fffffffffffffffffffffffffffffffffffffffffffffff9677777777777777776699999999999999999999667777777777777777777fffffffffff1111dffffff1fffffffffffffffffffffffffffff
        fffffffffffff1ffffffffffffffffffffffffffffffffff667777777777777777699999999999999999999966777777777777777777fffffffffd1111ddffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff6777777777777777769999999999999999999999966777777777777777fffffffffdd1111dddfffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff6677777777777777766999999999999999999999966777777777777777fffffffffd11111111dffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff677777777777777777699999999999999999999999677777777777777ffffffffffd11111111dffffffffffffffffffffffffffffffffff
        ffffffffffffffffff111111fff44ffffffffffffffffffffff777777777777777769999999999999999999999967777777777777ffffffffffffd1111d11dfffffffffffffffff5ffffffffffffffff
        fffffffffffffff1111eeee111445fffffffffffffffffffffff7677777777777776999999999999999999999996677777777777fffffffffffffff111ddddffffffffffffffff555fffffffffffffff
        ffffffffffffff11eeeeeeeee4455ffffffffffffffffffffffff66777777777777669999999999999999999999667777777777ffffffffffffffffff111dffffffffffff1fffff5ffffffffffffffff
        fffffffffffff11eeeeee44444555fffffffffffffffffffffffff667777777777776999999999999999999999966777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff11eeeeee444555555ffffffffffffffffffffffffff6677777777777699999999999999999999996677777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff1eeeeeeeee455555555ffffffffffffffffffffffffff66677777777769999999999999999999999677777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffff1eeeeeeeeeee555555555fffffffffffffffffffffffffff66677777776999999999999999999999667777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffff1eeeeeeeeee455555555555ffffffffffffff1ffffffffffff6677777769999999999999999999996777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1eeeeeeee1e4555555555555ffffffffffffffffffffffffffff6667777669999999999999999999667777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1eeeeee1114555555555555fffffffffffffffffffffffffffffff666677699999999999999999996666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1eeee11fffffffff5555fffffffffffffffffffffffffffffffffffff667699988888899999999966ffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffff1ffffffff
        ffffffff11eee11fffffffffff55fffffffffffffffffffffffffffffffffffffffff698888888888899999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffff11ee11ffffffffffff55ffffffffffffffffffffffffffffffffffffffffffffff888888888888ffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffff
        ffffffff11e11ffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffff
        fffffffff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffff1fffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffff
        fffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffff1ffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff4f4ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffff444ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff5fffffffffffffffffff4f4ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffff
        ffffffffffffffffffffffffffffffffffff555ffffffffffffffffff444ffffffffffffffff1ffffffffffffffffffffffffffffffff1fffff5ffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffff555ffffffffff1ffffffff
        ffffffffffffffffff5fffffffff1fffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffff
        fffffffffffffffff555fffffffffffffffffffffffffffff1fffffffffffffffff1fffffff555ffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffffffff5fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555ffffffffffff1fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
music.play(music.string_playable("- C D E F E D C ", 85),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.show_long_text("Ahh, Earth.", DialogLayout.BOTTOM)
game.show_long_text("It may not look it, but things have drastically changed since 20XX.",
    DialogLayout.BOTTOM)
game.show_long_text("How drastically? See for yourself!", DialogLayout.BOTTOM)
scene.set_background_image(img("""
    1111111111111111111111111199999999999999911111111111111111111111111119999999999111111111111111111111199999999999999999999944499999999111111555555555555555555555
        1111111111111111111111111199999999999991111111111111111111111111111111999999999111111111111111111111199999999999999999994449999999999111111555555555555555555555
        1111111111111111111111111199999999999991111111111111111111111111111111999999999111111111111111111111199999999999999944449999999999999111115555555555555555555555
        1111111111111111111111111199999999999911111111111111111111111111111111999999999111111111111111111111199999999999944449999999999999999111115555555555555555555555
        1111111111111111111111111199999999999911111111111111111111111111111111999999999911111111111111111111199999999994449999999999944449999111115555555555555555555555
        1111111111111111111111111999999999999991111111111111111111111111111111999999999991111111119111111111999999999999999999999944449999999111115555555555555555555555
        1111111111119111111111119999999999999991111111111111111111111111111119999999999999999999999991111111999999999999999999444444999999999111115555555555555555555555
        1111111111199991111111199999999999999999999999999111111119111111111199999999999999999999999999999999999999999999999444444999999999999111115555555555555555555555
        9111111111999999999999999999999999999999999999999911111199911111111999999999999999999999999999999999999999999999944499999999999999999111115555555555555555555555
        9999999999999999999999999999999999999999999999999999999999999911119999999999999999999999999999999999999999999994449999999999999994999111115555555555555555555555
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999994999999999999994444999111115555555555555555555555
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999444999999911115555555555555555555555
        99999999999999999999999999999999999999999999999999999999999ccccccc999bbbbccc999999999999888999999999888998999999999999994444499999999911115555555555555555555555
        999999999998899999999999888889999999999ccc99999999988889999cccbbbcc99999ccc9999999999988881119999998888888999999999999444999999999999911111555555555555555555555
        999999988888811119999988889999911199bbbbccc999999988889999cbbb111bcc99999999999999999999999999999998888811111999999944499999999999999991111555555555555555555555
        99999998888811111199988889991111119999999999999999888888991111111bbcc9999999999999999999999999999999999999999999999999999999999999999991111155555555555555555555
        999999999999999911999999999999911119999999999999999999999cbbbb111bbbbcc99999999999bbbbcc999999999999999999999999999999999999999994449999111155555555555555555555
        9999999999999999999999999999999999999999999999999999999ccbbbbbbbbbbbbbcccccc999999999cccc999999999999999999bbbbcc99999999999999944999999111115555555555555555555
        999999999999999999999999999999999999999999999999999999ccbbbbbbbbbbbbbbbbbbbc9999999999999999999999999999999999cccc9999999999994499999999911111555555555555555555
        999999999999999999999999999999999999999999999999999ccccbbbbbbbbbbbbbbbbbbbbc999999999999999999999999999999999999999999999999944999999999991111155555555555555555
        99999999999999999999999999999999999999999999999999ccbbbbbbbbbbbbbbbbbbbbbbbc999999999999999999999999999999999999999999999994449999999999999111115555555555555555
        99999999999999999999999999999999999999999999999999cbbbbbbbbbbbbbbbbbbbbbbbbcccc999999999999999999999999999999999999999999944999999999999999911111155555555555555
        99999999999999999999999999999999999999999999999999cbbbbbbbbbbbbbbbbbbbbbbbbbbbc999999999999999999999999999999999999999999999999999999999999991111111555555555551
        99999999999999999999999999999999999999999999999999ccbbbbbbbbbbbbcccbbbbbbbbbbbbc99999999999999999999999999999999999999999999999999999944999999111111111111111111
        999999999999999999999999999999999999999999999999999ccbbbbbbbbbbbbccbbbbbbbbbcccc99999999999999999999999999999999999999999999999999999449999999911111111111111111
        999999999999999999999999999999999999999999999999889ccbbbbbbbbbbbbcccbbbbbcccccc999999999999999999999999999999999999999999999999999994499999999999111111111111111
        999999999999999999999999999999999999999999988898889cbbbcccbbbbbbbcccbccccccccc9199999999999889999999999999999999999999999999999999999999999994499991111111111111
        999999999999999999999999999999999999999999988898889cbbbccccccccbbcccccccccccc99888999999999888999999999999999999999999999999999999999999999999999999991111111111
        999999999999999999999999999999999999999999998999899cbbbcccccccccccccccccc999991888999999999888999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999998999899ccccbccccccccccccccc99999988888889999998888899999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999998888888889999cbbbc9ccccccccccc99999988888889999998888899999999999999999999999999999999999999999988888888889999999999999
        999999999999999999999999999999999999999998888888889999ccccc999ccccccccc99999988888889999998888899999999999999999999999999999999999999999988888888889999999999999
        9999999999999999999888999999999999999999981188888899999cc999999cccccccc99999981188889999988888889999999999999999999988999999999999999999988181888889999999999999
        999999999999999999888889999999999999999998888888189999999999999cccccccc99999988888889999988888889999999999999999999888899999999999999999988888811889999999999999
        999999999999999998888889999999999999999998888888889999999999899cccccc8888899981888889999988888889999999999999999988888899999999999999999988888888889999999999999
        9999999999999999988818999999899999999999988888888899999999988999ccccc8888899988888889999988888889999999999999999988818999999889999999999988881888889999999988999
        9999999999999999988888899999899999999999988888881899999999988999ccccc8888899988888889999988888889999999999999999988888899999889999999999988888881889999999988999
        9999999988899999988118999998889999999999988888888899888888988999ccccc8888899988888889999988888889999999998899999988818999998889999999999988888888889888888888999
        898899998888888898818889998888899999999998888888189981188898899ccccccc881889988888889998888888888988999988888888888881899998888999999999988888811889811888888999
        888899999818818898888889998888899999999998888888889988881898899cccccc8888889988188889998888888888888999988188818888888899998888999999999988888888889888818888999
        881899999888111198888889998888899999999998888888889988881888899cccccc8888889988888889998888888888818999988881811888888899998888999999999988888888889888818888999
        888899998888888898888888998888889988988988888888888981188888899cccccc8888889988888889998888888888888999988888888888888889988888899989988888888888889811888888999
        8818999988888888988888889988888899888888888888888889888888888998cc8cc8888889988888889998888888888818999988888888888888889988888899988888888888888889888888888999
        8888898818188888988888889988888889888811888888888888811bb8888888c888cc88188998888888999888888888888888988818888888888888998888888999811888888b888888811bbb888988
        8888898888888888888888888818888889888888888bbb888888888bbb888888c888c88888899888888899988888888888888898888888888888888888888888898888888888bb888888888bbb888988
        8888898888888888888888888888888889888888888bbb888888888bbb8888888888888888888888888899988888888888888898888888888888888888888888898888888888bb888888888bbb888888
        88888988888888888888888888888888898888888bbbbbbb888888bbbbb8888888888888888888888888889888888888888888988888888888888888888888888981888888bbbbbbb88888bbbbb88888
        88888bbbbbbbbb888888888888888888898888888bbbbbbb888888bbbbb888888888888888888888888888988888888888888bbbbbbbbbb888888888888888888988888888bbbbbbb88888bbbbb88888
        88888bbbbbbbbb888888888888888888898888888bbbbbbb888888bbbbb888888888888888888888888888988888888888888bbbbbbbbbb888888888888888888988888888bbbbbbb88888bbbbb88888
        88888bddbbbbbb888888888888888888898888888bddbbbb88888bbbbbbb88111888888888888888bb8888988888888888888bbdbdbbbbb888888888888888888988888888bbbbbbb8888bbbbbbbb118
        88888bbbbbbbdb888888888888888888898888888bbbbbbb88888bbbbbbb8881188888888888888bbbb888988888888888888bbbbbbddbb888888888888888888988888888bbbbbbb8888bbbbbbbb888
        88888bbbbbbbbb8888888888b88888888bbbbb888bdbbbbb88888bbbbbbb88888888888188888bbbbbb888988888888888888bbbbbbbbbb8888888888888888888bbbb8888bbbdbbb8888bbbbbbbb888
        88888bbbbbbbbb888888888bb88888888bbbbb888bbbbbbb88888bbbbbbb88188888888888888bbbdb888888bb88888888888bbbbdbbbbb88888888bb888888888bbbb8888bbbdbbb8888bbbbbbbb818
        88888bbbbbbbdb888888888bb88888888bbbbb888bbbbbbb88888bbbbbbb88111888888888888bbbbbb88888bb88888888888bbbbbbbdbb88888888bb88888888bbbbbb888bbbbbbb8888bbbbbbbb118
        88888bbbbbbbbb88bbbbbb8bb88888888bbbbb888bbbbbbb88888bbbbbbb888888888bb188888bbbdb88888bbb88888888888bbbbbbbbbb8bbbbbbbbb88888888bbbbbb888bbbdbbb8888bbbbbbbb888
        88888bbbbbbbdb88bddbbb8bb888888888bbdbb88bbbbbbb888bbbbbbbbbb8bb8888bbbbbbbbbbbbbdb8888bbbb8888888888bbbbbbddbb8bddbbbbbb88888888bbbbbbb88bbbbbbb88bbbbbbbbbbbbb
        88888bbbbbbbbb88bbbbdb8bb88888888bbbbbb88bbdbbbb888bbbbbbbbbbbbb8888bbdbbbdbbbbbbbb8888bbbb8888888888bbbbbbbbbb8bbbbdbbbb88888888bbbbbbb88bbbbdbb88bbbbbbbbbbbbb
        88888bbbbbbbbb88bbbbdbbbb88888888bbbbbb88bbbbbbb888bbbbbbbbbbbdb8888bbbbdbddbbbbbbb8888bbbb8888888888bbbbbbbbbb8bbbbdbbbb88888888bbbbbbb88bbbbbbb88bbbbbbbbbbbbb
        8bb8bbbbbbbbbbb8bddbbbbbb88888888bbbbbb88bbbbbbb888bbbbbbbbbbbbb8888bbbbbbbbbbbbbbbb88bbbbbb888b88bbbbbbbbbbbbb8bddbbbbbb88888888bbbbbbb88bbbbbbb88bbbbbbbbbbbbb
        bbbbbbbbbbbbbbb8bbbbbbbbb88b88b88bbb3bb88bbbbbbb888bbbbbbbbbbbdb8888bbbbbbbbbbbbbbbb88bbbbbb888bbbbbbbbbbbbbbbb8bbbbbbbbb88888b88bbbbbbb88bbbbbbb88bbbbbbbbbbbbb
        bbddbbbbbbbbbbbbbddddbbbbbbb8bbb88bbdbb88bbbbbbb888bbbbbbbbbbbbbbb8bbbdbbbbbbbbbbbbb88bbbbbbb888bddbbbbbbbbbbbbbbddbdbbbb8bb8bbb8bbbbbbb88bbbbbbb88bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbb8bbbbbb88bbbbbbb888bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbb8bb8bbbbbbbbbbb88bbbbdbb88bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb888bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbb8bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbb
        bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7
        bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77
        bb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777b
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777766666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777776655667777777776666666666777777777777777777777776677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777776667777675556677777665555555557666777777777777777777666567777777667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777666777677755667766555777777766667777777777777777777675567777777667777777777777777777777777777677777777777777777777777777777777777777777777777777777777777
        7777777665567667777566655577777776667777777777777777777776755667777777666777777777777777777777777777666777777777777777777777777777777777777777777777777777777777
        7777777767567767777556557777777766777777777777777777777776757677777776676777777777777777777777777777656677777777777777777777777777777777777777777777777777777777
        7777777766755767777755557777777667777777777777777777777765557677777776776777777777777777777777777777765677777777777777777777777777666777777777777777777777777777
        7777777776775677777775657777777677777777777777777777777765577677777766776777777777777777777777777777767567777777777777777777777766576777777777777777777777777777
        7777777776775567777775567777777677777777777777777777777765577677777667776777777777777777777777777777766756777777777777777777776655576777777777777777777777777777
        7777777777677567777777567777776777777777777777777777777665577667776677776777777777777777777777777777776775677777777777777777765555776777777777777777777777777777
        7777777777677556777777567777776777777777777777777777777655577767666777776777777777777777777777777777776775667777777777777777655555776777777777777777777777777777
        7777777777677755777777567777776777777777777777777777777655577766777777776777777777777777777777777777776775567777777777777776555557776777777777777777777777777777
        7777777777677775677777767777776777777777777777777777777655577767777777776777777777777777777777777777776777556777777777777765555557776777777777777777777777777777
        7777777777677775677777767777776777777777777777777777777655577776777777776777777777777777777777777777766777556777777777777765555577776777777777777777777777777777
        7777777777677775677777767777776777777777777777777777777655577776777777766777777777777777777777777777767777556777777777777765555577776777777777777777777777777777
        7777777777677777677777767777776777777777777777777777776655577776777777767777777777777777777777777777767777756777777777777765555577776777777777777777777777777777
        7777777777677777767777767777776777777777777777777777766655577777677777677777777777777777777777777777677777755677777777777765555577776677777777777777777777777777
        7777777777677777767777767777776777777777777777777777667655577777767777677777777777777777777777777777677777775677777777777765555577777677777777777777777777777777
        7777777777677777767777767777776777777777777777777776677655557777767776777777777777777777777777777776677777775677777777777776555577777677777777777777777777777777
        7777777776777777767777767777776777777777777777777766777655557777776766777777777777777777777777777766777777775677777777777776555577777767777777777777777777777777
        7777777776777777767777767777776677777777777777777667777655555777776667777777777777777777777777777767777777755677777777777776655577777776777777777777777777777777
        7777777776777777767777767777777677777777777777777677777665555777777677777777777777777777777777777667777777757677777777777777655557777776677777777777777777777777
        7777777767777777767777667777777667777777777777776677777765555577777767777777777777777777777777776677777777756777777777777777665557777777667777777777777777777777
        7777777767777777767777677777777767777777777777776777777776555557777766777777777777777777777777766777777777756777777777777777766557777777766777777777777777777777
        7777777677777777677777677777777776677777777777776777777776655557777776677777777777777777777777667777777777556777777777777777776555777777776677777777777777777777
        7777776677777777677777677777777777667777777777776777777777655555777777667777777777777777777776677777777775566777777777777777777655577777777666777777777777777777
        7777776777777776677776777777777777766777777777776777777777766555577777776777777777777777777666777777777755667777777777777777777766577777777776666777777777777777
        7777767777777776777776777777777777776677777777776777777777776655555777777667777777777777776677777777777757677777777777777777777776557777777777776677777777777777
"""))
game.show_long_text("Nice scenery, eh?", DialogLayout.BOTTOM)
game.show_long_text("Ever since the lovely Future Org started running things around here, our technology is entirely dependent on the sun!  ",
    DialogLayout.BOTTOM)
game.show_long_text("We all benefit from this, y'know? Less carbon emissions, less global warming happening... , ",
    DialogLayout.BOTTOM)
game.show_long_text("Plus, we've got all these plants and trees everywhere! Don't you just love clean fresh air?!",
    DialogLayout.BOTTOM)
game.show_long_text("It's just perfect!", DialogLayout.BOTTOM)
game.show_long_text("With all of this, nothing could ever go-",
    DialogLayout.BOTTOM)
music.stop_all_sounds()
music.play(music.create_sound_effect(WaveShape.NOISE,
        2245,
        2188,
        183,
        0,
        1475,
        SoundExpressionEffect.WARBLE,
        InterpolationCurve.LOGARITHMIC),
    music.PlaybackMode.UNTIL_DONE)
game.show_long_text("...wrong?... What was that?", DialogLayout.BOTTOM)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff1fffffffffffffff1fffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffff1fffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888fffbbbbcccffffffffffff888fffffffff888ff8ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff88fffffffffff88888ffffffffffcccfffffffff8888ffff888bbb88fffffcccfffffffffff8888111ffffff8888888ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffff8888881111fffff8888fffff111ffbbbbcccfffffff8888ffffcbbb111988fffffffffffffffffffffffffffffff8888811111fffffffffffffffffffffffffffffffffffffffffffffffffff
        fff1fff88888111111fff8888fff111111ffffffffffffffff888888ff11111119988fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffff11fffffffffffff1111fffffffffff1ffffffffffc9999111999988fffffffffffbbbbccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff889999999999999888888fffffffffccccffffffffffffffffffbbbbccffffffffffffffffffff1fffffffffff1ffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff1fffffffffff8899999999999999999998ffffffffffffffffffffffffffffffffffccccfffffff1ffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff8888999999999999999999998ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff88999999999999999999999998ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff89999999999999999999999998888fffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff89999999999999999999999999998fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff889999999999998889999999999998ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffff1fffffffffffffffff1fffffffffffffff88999999999999889999999998888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffff1fffffffffffffffffffffffffffffffffffffffffccf8899999999999988899999888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffff1ffffffff
        ffffffffffffffffffffffff1ffffffffffffffffffcccfcccf899988899999998889888888888f1fffffffffffccfffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffcccfcccf89998888888899888888888888ffcccfffffffffcccffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffcfffcff8999888888888888888888fffff1cccfffffffffcccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffcfffcff88889888888888888888ffffffcccccccffffffcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffcccccccccffff89998f88888888888ffffffcccccccffffffcccccffffffffffffffffffffffffffffffffffffffffffccccccccccfffffffffffff
        fffffffffffffffffffffffffffffffffffffffffcccccccccffff88888fff888888888ffffffcccccccffffffcccccffffffffffffffffffffffffffffffffffffffffffccccccccccfffffffffffff
        fffffffffffffffffffcccfffffffffffffffffffc11ccccccfffff88ffffff88888888ffffffc11ccccfffffcccccccffffffffffffffffffffccfffffffffffffffffffcc1c1cccccfffffffffffff
        ffffffffffffffffffcccccffffffffffffffffffccccccc1cfffffffffffff88888888ffffffcccccccfffffcccccccfffffffffffffffffffccccffffffffffffffffffcccccc11ccfffffffffffff
        fffffffffffffffffccccccffffffffffffffffffcccccccccffffffffffcff888888cccccfffc1cccccfffffcccccccfffffffffffffffffccccccffffffffff1fffffffccccccccccfffffffffffff
        fffffffffffffffffccc1cffffffcffffffffffffcccccccccfffffffffccfff88888cccccfffcccccccfffffcccccccfffffffffffffffffccc1cffffffccfffffffffffcccc1cccccffffffffccfff
        fffffffffffffffffccccccfffffcffffffffffffccccccc1cfffffffffccfff88888cccccfffcccccccfffffcccccccfffffffffffffffffccccccfffffccfffffffffffccccccc1ccffffffffccfff
        ffffffffcccffffffcc11cfffffcccfffffffffffcccccccccffccccccfccfff88888cccccfffcccccccfffffcccccccfffffffffccffffffccc1cfffffcccfffffffffffccccccccccfcccccccccfff
        cfccffffccccccccfcc1cccfffcccccffffffffffccccccc1cffc11cccfccff8888888cc1ccffcccccccfffccccccccccfccffffccccccccccccc1cffffccccffffffffffcccccc11ccfc11ccccccfff
        ccccfffffc1cc1ccfccccccfffcccccffffffffffcccccccccffcccc1cfccff888888ccccccffcc1ccccfffcccccccccccccffffcc1ccc1ccccccccffffccccffffffffffccccccccccfcccc1ccccfff
        cc1cfffffccc1111fccccccfffcccccffffffffffcccccccccffcccc1ccccff888888ccccccffcccccccfffccccccccccc1cffffcccc1c11cccccccffffccccffffffffffccccccccccfcccc1ccccfff
        ccccffffccccccccfcccccccffccccccffccfccfcccccccccccfc11ccccccff888888ccccccffcccccccfffcccccccccccccffffccccccccccccccccffccccccfffcffcccccccccccccfc11ccccccfff
        cc1cffffccccccccfcccccccffccccccffcccccccccccccccccfcccccccccffc88c88ccccccffcccccccfffccccccccccc1cffffccccccccccccccccffccccccfffccccccccccccccccfcccccccccfff
        cccccfcc1c1cccccfcccccccffcccccccfcccc11ccccccccccccc1166ccccccc8ccc88cc1ccffcccccccfffcccccccccccccccfccc1cccccccccccccffcccccccfffc11cccccc6ccccccc11666cccfcc
        cccccfcccccccccccccccccccc1ccccccfccccccccc666ccccccccc666cccccc8ccc8ccccccffcccccccfffcccccccccccccccfccccccccccccccccccccccccccfcccccccccc66ccccccccc666cccfcc
        cccccfcccccccccccccccccccccccccccfccccccccc666ccccccccc666ccccccccccccccccccccccccccfffcccccccccccccccfccccccccccccccccccccccccccfcccccccccc66ccccccccc666cccccc
        cccccfcccccccccccccccccccccccccccfccccccc6666666cccccc66666cccccccccccccccccccccccccccfcccccccccccccccfccccccccccccccccccccccccccfc1cccccc6666666ccccc66666ccccc
        ccccc666666666cccccccccccccccccccfccccccc6666666cccccc66666cccccccccccccccccccccccccccfcccccccccccccc6666666666ccccccccccccccccccfcccccccc6666666ccccc66666ccccc
        ccccc666666666cccccccccccccccccccfccccccc6666666cccccc66666cccccccccccccccccccccccccccfcccccccccccccc6666666666ccccccccccccccccccfcccccccc6666666ccccc66666ccccc
        ccccc6dd666666cccccccccccccccccccfccccccc6dd6666ccccc6666666cc111ccccccccccccccc66ccccfcccccccccccccc66d6d66666ccccccccccccccccccfcccccccc6666666cccc6666666611c
        ccccc6666666d6cccccccccccccccccccfccccccc6666666ccccc6666666ccc11cccccccccccccc6666cccfcccccccccccccc666666dd66ccccccccccccccccccfcccccccc6666666cccc66666666ccc
        ccccc666666666cccccccccc6cccccccc66666ccc6d66666ccccc6666666ccccccccccc1ccccc666666cccfcccccccccccccc6666666666ccccccccccccccccccc6666cccc666d666cccc66666666ccc
        ccccc666666666ccccccccc66cccccccc66666ccc6666666ccccc6666666cc1cccccccccccccc666d6cccccc66ccccccccccc6666d66666cccccccc66ccccccccc6666cccc666d666cccc66666666c1c
        ccccc6666666d6ccccccccc66cccccccc66666ccc6666666ccccc6666666cc111cccccccccccc666666ccccc66ccccccccccc6666666d66cccccccc66cccccccc666666ccc6666666cccc6666666611c
        ccccc666666666cc666666c66cccccccc66666ccc6666666ccccc6666666ccccccccc661ccccc666d6ccccc666ccccccccccc6666666666c666666666cccccccc666666ccc666d666cccc66666666ccc
        ccccc6666666d6cc6dd666c66ccccccccc66d66cc6666666ccc6666666666c66cccc6666666666666d6cccc6666cccccccccc666666dd66c6dd666666cccccccc6666666cc6666666cc6666666666666
        ccccc666666666cc6666d6c66cccccccc666666cc66d6666ccc6666666666666cccc66d666d66666666cccc6666cccccccccc6666666666c6666d6666cccccccc6666666cc6666d66cc6666666666666
        ccccc666666666cc6666d6666cccccccc666666cc6666666ccc66666666666d6cccc6666d6dd6666666cccc6666cccccccccc6666666666c6666d6666cccccccc6666666cc6666666cc6666666666666
        c66c66666666666c6dd666666cccccccc666666cc6666666ccc6666666666666cccc6666666666666666cc666666ccc6cc6666666666666c6dd666666cccccccc6666666cc6666666cc6666666666666
        666666666666666c666666666cc6cc6cc666366cc6666666ccc66666666666d6cccc6666666666666666cc666666ccc6666666666666666c666666666ccccc6cc6666666cc6666666cc6666666666666
        66dd6666666666666dddd6666666c666cc66d66cc6666666ccc666666666666666c666d6666666666666cc6666666ccc6dd66666666666666dd6d6666c66c666c6666666cc6666666cc6666666666666
        6666666666666666666666666666c666c666666cc6666666ccc666666666666666c66666666666666666666666666c666666666666666666666666666c66c66666666666cc6666d66cc6666666666666
        666666666666666666666666666666666666666666666666ccc666666666666666c66666666666666666666666666c666666666666666666666666666666666666666666666666666cc6666666666666
        66666666666666666666666666666666666666666666666666c666666666666666c66666666666666666666666666c6d66666666666666666666666666666666666666666666666666c6666666666666
        66666666666666666666666666666666666666666666666666c666666666666666c66666666666666666666666666c66666666666666666666666666666666d6666666666666666666c6666666666666
        66666666666666666666666666666666666666666666666666c666666666666666c66666666666666666666666666c6666666666666666666666666666666666666666666666666666c6666666666666
        66666666666666666666666666ddd666666666666666666666c666666666666666c66666666666666666666666666c666666666666666666666666666dd6d6d666666666666666666666666666666666
        666666666666666666666666666dd666666666666666666666c666666666666666c66666666666666666666666666c666666666666666666666666666666d6d666666666666666666666666666666666
        66666666666666666666666666666666666d66666666666666c666666666666666666666666666666666666666666666666666666666666666666666666666d6666d6666666666666666666666666666
        66666666666666666666666666d66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666d6666666666666666666666666666666666666
        66666666666666666666666666ddd66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666dd6d66666666666666666666666666666666666
        66666666666666666666666666666666666d6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666686666666666666666866666666666666666666668666666666666666686666666666666666666666866666666666666668666666666666666666666686666666666666666866666
        6666668666886666688666686668666686886668666666866688666668866668666866668688666866666686668866666886666866686666868866686666668666886666688666686668666686886668
        6686668868866866688666886668866686688688668666886886686668866688666886668668868866866688688668666886668866688666866886886686668868866866688666886668866686688688
        668866886886688666886886666886868868888666886688688668866688688666688686886888866688668868866886668868866668868688688886668866886886688666886886666886868868888b
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888666688888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888866666688888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888886677668888888886666666666888888888888888888888886688888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888886668888687776688888667777777777666888888888888888888666768888888668888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888666888688877668866777888888866668888888888888888888677768888888668888888888888888888888888888688888888888888888888888888888888888888888888888888888888888
        8888888667768668888766677788888886668888888888888888888886777668888888666888888888888888888888888888666888888888888888888888888888888888888888888888888888888888
        8888888867768868888776778888888866888888888888888888888886778688888886686888888888888888888888888888656688888888888888888888888888888888888888888888888888888888
        8888888866877868888877778888888668888888888888888888888867778688888886886888888888888888888888888888865688888888888888888888888888666888888888888888888888888888
        8888888886887688888887678888888688888888888888888888888867788688888866886888888888888888888888888888867568888888888888888888888866786888888888888888888888888888
        8888888886887768888887768888888688888888888888888888888867788688888668886888888888888888888888888888866856888888888888888888886677786888888888888888888888888888
        8888888888688768888888768888886888888888888888888888888667788668886688886888888888888888888888888888886887688888888888888888867777886888888888888888888888888888
        8888888888688776888888768888886888888888888888888888888677788868666888886888888888888888888888888888886887668888888888888888677777886888888888888888888888888888
        8888888888688877888888768888886888888888888888888888888677788866888888886888888888888888888888888888886887768888888888888886777778886888888888888888888888888888
        8888888888688887688888868888886888888888888888888888888677788868888888886888888888888888888888888888886888776888888888888867777778886888888888888888888888888888
        8888888888688887688888868888886888888888888888888888888677788886888888886888888888888888888888888888866888776888888888888867777788886888888888888888888888888888
        8888888888688887688888868888886888888888888888888888888677788886888888866888888888888888888888888888868888776888888888888867777788886888888888888888888888888888
        8888888888688888688888868888886888888888888888888888886677788886888888868888888888888888888888888888868888876888888888888867777788886888888888888888888888888888
        8888888888688888868888868888886888888888888888888888866677788888688888688888888888888888888888888888688888877688888888888867777788886688888888888888888888888888
        8888888888688888868888868888886888888888888888888888668677788888868888688888888888888888888888888888688888887688888888888867777788888688888888888888888888888888
        8888888888688888868888868888886888888888888888888886688677778888868886888888888888888888888888888886688888887688888888888886777788888688888888888888888888888888
        8888888886888888868888868888886888888888888888888866888677778888886866888888888888888888888888888866888888887688888888888886777788888868888888888888888888888888
        8888888886888888868888868888886688888888888888888668888677777888886668888888888888888888888888888868888888877688888888888886677788888886888888888888888888888888
        8888888886888888868888868888888688888888888888888688888667777888888688888888888888888888888888888668888888877688888888888888677778888886688888888888888888888888
        8888888868888888868888668888888668888888888888886688888867777788888868888888888888888888888888886688888888878888888888888888667778888888668888888888888888888888
        8888888868888888868888688888888868888888888888886888888886777778888866888888888888888888888888866888888888878888888888888888866778888888866888888888888888888888
        8888888688888888688888688888888886688888888888886888888886677778888886688888888888888888888888668888888888778888888888888888886777888888886688888888888888888888
        8888886688888888688888688888888888668888888888886888888888677777888888668888888888888888888886688888888887788888888888888888888677788888888666888888888888888888
        8888886888888886688886888888888888866888888888886888888888866777788888886888888888888888888666888888888877888888888888888888888866788888888886666888888888888888
        8888868888888886888886888888888888886688888888886888888888886677777888888668888888888888886688888888888877888888888888888888888886778888888888886688888888888888
"""))
music.play(music.string_playable("E - C5 G - F C5 B ", 600),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.show_long_text("....Um... That's.... not good...", DialogLayout.BOTTOM)
game.show_long_text("You! Yeah, you! I know we've only known each other for 20 seconds, but please!",
    DialogLayout.BOTTOM)
game.show_long_text("Help us! Without the sun, we're literally about to go extinct! ",
    DialogLayout.BOTTOM)
game.show_long_text("We based literally EVERYTHING, our livelyhoods surrounded with the sun in mind!",
    DialogLayout.BOTTOM)
game.show_long_text("Without it, we have no power, no food, basically EVERYTHING's about to go bad!",
    DialogLayout.BOTTOM)
game.show_long_text("What's worse, if the TREE OF LIFE dies because of the sun's disappearance, it's a guaranteed death for this planet!",
    DialogLayout.BOTTOM)
game.show_long_text("So please! Help us bring back the sun!",
    DialogLayout.BOTTOM)
story.show_player_choices("Of course!", "Nah, it's not my problem")
if story.check_last_answer("Of course!"):
    game.show_long_text("Ahh, thank you! Let's hurry, it's getting a bit around here already...",
        DialogLayout.BOTTOM)
else:
    game.show_long_text("Well, that's too bad. We didn't ask to be in this situation, so it is your problem now. C'mon, save us already. It's getting too cold around here.",
        DialogLayout.BOTTOM)
current_level += 1
music.stop_all_sounds()
music.play(music.string_playable("C - G - B - G - ", 500),
    music.PlaybackMode.UNTIL_DONE)
music.play(music.create_song(hex("""
        0078000408190203001c0001dc00690000045e01000400000000000000000000056400010400030e0140004800012450005800012560006800012468007000012070007800012c78008000012c8000880001279000980001299800a0000124a000a8000127b800bc00011dbc00c0000120c000c8000127d000d8000129d800e0000124e000e8000127f8000001012700010801012908011001012410011801012718012001012420012801012240014801012450015801012560016801012468017001012070017801012c78018001012c80018801012790019801012998019c010124a001a8010127b801bc01011dbc01c0010120c001c8010127d001d801012cd801e001012ce001e8010125f001f801012cf8010002012c00020802012a08021002012a10021802012c18022002012a20022802012c05001c000f0a006400f4010a0000040000000000000000000000000000000002600300000400012204000800012008000c00011b0c001000012010001400012214001800012018001c00011b1c002000012020002400012224002800012028002c00011b2c003000012030003400012234003800012038003c00011b3c004000012040004400012244004800012048004c00011b4c005000012050005400012254005800012058005c00011b5c006000012060006400012264006800012068006c00011b6c007000012070007400012274007800012078007c00011b7c008000012080008400012284008800012088008c00011b8c009000012090009400012294009800012098009c00011b9c00a0000120a000a4000122a400a8000120a800ac00011bac00b0000120b000b4000122b400b8000120b800bc00011bbc00c0000120c000c4000122c400c8000120c800cc00011bcc00d0000120d000d4000122d400d8000120d800dc00011bdc00e0000120e000e4000122e400e8000120e800ec00011bec00f0000120f000f4000122f400f8000120f800fc00011bfc000001012000010401012204010801012008010c01011b0c011001012010011401012214011801012018011c01011b1c012001012020012401012224012801012028012c01011b2c013001012030013401012234013801012038013c01011b3c014001012040014401012244014801012048014c01011b4c015001012050015401012254015801012058015c01011b5c016001012060016401012264016801012068016c01011b6c017001012070017401012274017801012078017c01011b7c018001012080018401012284018801012088018c01011b8c019001012090019401012294019801012098019c01011b9c01a0010120a001a4010122a401a8010120a801ac01011bac01b0010120b001b4010122b401b8010120b801bc01011bbc01c0010120c001c4010122c401c8010120c801cc01011bcc01d0010120d001d4010122d401d8010120d801dc01011bdc01e0010120e001e4010122e401e8010120e801ec01011bec01f0010120f001f4010122f401f8010120f801fc01011bfc010002012000020402012204020802012008020c02011b0c021002012010021402012214021802012018021c02011b1c022002012020022402012224022802012028022c02011b2c023002012030023402012234023802012038023c02011b3c0240020120
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
nothing()
scene.set_background_color(15)
scene.set_background_image(img("""
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
"""))
playersprite = sprites.create(img("""
        . . . . . e e e e e . . . . . . 
            . . . . e e e e e e e . . . . . 
            . . . . e e 4 e 4 e e . . . . . 
            . . . e e b f d f b e e . . . . 
            . . . e e 1 f d f 1 e e . . . . 
            . . . e e 3 d d d 3 e e . . . . 
            . . . . e 6 d 2 d 6 e . . . . . 
            . . . . 6 9 9 d 9 9 6 . . . . . 
            . . . 6 9 9 9 9 9 9 9 6 . . . . 
            . . . 4 4 9 9 9 9 9 4 4 . . . . 
            . . . d d 9 9 9 9 9 d d . . . . 
            . . . . . 8 9 9 9 8 . . . . . . 
            . . . . . 8 8 f 8 8 . . . . . . 
            . . . . . 8 8 f 8 8 . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
info.set_life(16)
house = sprites.create(img("""
        ....................e2e22e2e....................
            .................222eee22e2e222.................
            ..............222e22e2e22eee22e222..............
            ...........e22e22eeee2e22e2eeee22e22e...........
            ........eeee22e22e22e2e22e2e22e22e22eeee........
            .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
            ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
            4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
            6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
            46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
            46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
            4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
            6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
            4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
            6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
            46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
            6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
            46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
            46622e22e22e22eeecc6666666666cceee22e22e22e22664
            4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
            6c622e22eeecc66666cc64444446cc66666cceee22e226c6
            46622e22cc66666cc64444444444446cc66666cc22e22664
            46622cc6666ccc64444444444444444446ccc6666cc22664
            4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
            cccccccc6666666cb44444444444444bc6666666cccccccc
            64444444444446c444444444444444444c64444444444446
            66cb444444444cb411111111111111114bc444444444bc66
            666cccccccccccd166666666666666661dccccccccccc666
            6666444444444c116eeeeeeeeeeeeee611c4444444446666
            666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
            666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
            666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
            666edffdffde4c66f4effffffffff4ee66c4edffdffde666
            666edccdccde4c66f4effffffffffeee66c4edccdccde666
            666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
            c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
            c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
            cc66666666664c66e4e44e44e44feeee66c46666666666cc
            .c66444444444c66e4e44e44e44ffffe66c44444444466c.
            ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
            ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
            ....644444444c66f4e44e44e44e44ee66c444444446....
            .....64eee444c66f4e44e44e44e44ee66c444eee46.....
            ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
    """),
    SpriteKind.food)
mySprite2 = sprites.create(img("""
        . . . . . e e e e e . . . . . . 
            . . . . e e e e e e e . . . . . 
            . . . . e e 4 e 4 e e . . . . . 
            . . . e e b f d f b e e . . . . 
            . . . e e 1 f d f 1 e e . . . . 
            . . . e e 3 d d d 3 e e . . . . 
            . . . . e 6 d 2 d 6 e . . . . . 
            . . . . 6 9 9 d 9 9 6 . . . . . 
            . . . 6 9 9 9 9 9 9 9 6 . . . . 
            . . . 4 4 9 9 9 9 9 4 4 . . . . 
            . . . d d 9 9 9 9 9 d d . . . . 
            . . . . . 8 9 9 9 8 . . . . . . 
            . . . . . 8 8 f 8 8 . . . . . . 
            . . . . . 8 8 f 8 8 . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.npc)
animation.run_image_animation(playersprite,
    [img("""
            . . . . . e e e e e . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e b f d f b e e . . . . 
                . . . e e 1 f d f 1 e e . . . . 
                . . . . e d d d d d e . . . . . 
                . . . . f f 1 2 1 f f . . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f f c c c c c f f . . . . 
                . . . 4 4 c c c c c 4 4 . . . . 
                . . . d d c c c c c d d . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . f f f f f . . . . . .
        """),
        img("""
            . . . . . e e e e e . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e b f d f b e e . . . . 
                . . . e e 1 f d f 1 e e . . . . 
                . . . . e d d d d d e . . . . . 
                . . . . f f 1 2 1 f f . . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f c c 2 1 1 c c f . . . . 
                . . . d d c c c c c f f . . . . 
                . . . d d c c c c c 4 4 . . . . 
                . . . . . c c c c c 4 4 . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 . f f . . . . . . 
                . . . . . 8 8 . . . . . . . . .
        """),
        img("""
            . . . . . e e e e e . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e b f d f b e e . . . . 
                . . . e e 1 f d f 1 e e . . . . 
                . . . . e d d d d d e . . . . . 
                . . . . f f 1 2 1 f f . . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f f c c c c c f f . . . . 
                . . . 4 4 c c c c c 4 4 . . . . 
                . . . d d c c c c c d d . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . f f f f f . . . . . .
        """),
        img("""
            . . . . . e e e e e . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e b f d f b e e . . . . 
                . . . e e 1 f d f 1 e e . . . . 
                . . . . e d d d d d e . . . . . 
                . . . . f f 1 2 1 f f . . . . . 
                . . . f c c 1 2 1 c c f . . . . 
                . . . f c c 1 1 2 c c f . . . . 
                . . . f f c c c c c d d . . . . 
                . . . 4 4 c c c c c d d . . . . 
                . . . 4 4 c c c c c . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . 8 8 8 8 8 . . . . . . 
                . . . . . f f . 8 8 . . . . . . 
                . . . . . . . . 8 8 . . . . . .
        """)],
    200,
    True)
house.set_position(81, 140)
controller.move_sprite(playersprite)
scene.camera_follow_sprite(playersprite)
Change_Level(1)
mySprite = sprites.create(img("""
        . . . . . 5 5 5 5 5 . . . . . . 
            . . . . 5 5 5 5 5 5 5 . . . . . 
            . . . . 5 5 4 5 4 5 5 . . . . . 
            . . . 5 5 b f d f b 5 5 . . . . 
            . . . 5 5 1 f d f 1 5 5 . . . . 
            . . . 5 5 3 d d d 3 5 5 . . . . 
            . . . . 5 a d 2 d a 5 . . . . . 
            . . . . a 3 3 d 3 3 a . . . . . 
            . . . a 3 3 3 3 3 3 3 a . . . . 
            . . . 4 4 3 3 3 3 3 4 4 . . . . 
            . . . d d 3 3 3 3 3 d d . . . . 
            . . . . . c 3 3 3 c . . . . . . 
            . . . . . c c f c c . . . . . . 
            . . . . . c c f c c . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.theothernpc)
mySprite3 = sprites.create(img("""
        . . . . . e e e e e . . . . . . 
            . . . . e e e e e e e . . . . . 
            . . . . e e 4 e 4 e e . . . . . 
            . . . e e b f 4 f b e e . . . . 
            . . . e e 1 f 4 f 1 e e . . . . 
            . . . e e 3 4 4 4 3 e e . . . . 
            . . . . e c 4 2 4 c e . . . . . 
            . . . . c 7 7 d 7 7 c . . . . . 
            . . . c 7 7 7 7 7 7 7 c . . . . 
            . . . 4 4 7 7 7 7 7 4 4 . . . . 
            . . . d d 7 7 7 7 7 d d . . . . 
            . . . . . 5 7 7 7 5 . . . . . . 
            . . . . . 5 5 f 5 5 . . . . . . 
            . . . . . 5 5 f 5 5 . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Silly)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile27
"""))
tiles.place_on_random_tile(mySprite2, assets.tile("""
    myTile28
"""))
tiles.place_on_random_tile(mySprite3, assets.tile("""
    myTile36
"""))
mySprite4 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . f f f f f f f f f . . . . 
            . . f d d d d d d d e e f . . . 
            . f d f d f d d f d d e f . . . 
            . f d f f d f f d e e e f . . . 
            . f d d d d d d d e e f f . . . 
            . . f f f d d d e f f . . . . . 
            . . . . . f d e f . . . . . . . 
            . . . . . f d e f . . . . . . . 
            . . . . . f d e f . . . . . . . 
            . . . . . f d e f . . . . . . . 
            . . . . . . f f . . . . . . . .
    """),
    SpriteKind.sign)
tiles.place_on_random_tile(mySprite4, assets.tile("""
    myTile4
"""))
mySprite6 = sprites.create(img("""
        . . . . . 3 3 3 3 3 . . . . . . 
            . . . . 3 3 3 3 3 3 3 . . . . . 
            . . . . 3 3 2 3 2 3 3 . . . . . 
            . . . 3 3 b f d f b 3 3 . . . . 
            . . . 3 3 1 f d f 1 3 3 . . . . 
            . . . 3 3 d d d d d 3 3 . . . . 
            . . . . 3 f d 2 d f 3 . . . . . 
            . . . . f b b d b b f . . . . . 
            . . . f b b b b b b b f . . . . 
            . . . 4 4 b b b b b 4 4 . . . . 
            . . . d d b b b b b d d . . . . 
            . . . . . 2 b b b 2 . . . . . . 
            . . . . . 2 2 f 2 2 . . . . . . 
            . . . . . 2 2 f 2 2 . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.shopkind)
tiles.place_on_tile(mySprite6, tiles.get_tile_location(5, 12))