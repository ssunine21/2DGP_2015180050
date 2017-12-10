import main_game


def handle_move_GIRL(frame_time):

    # 모든 몬스터와 함정이 앞으로 당겨짐

    main_game.stage1_map.handle_move(frame_time)
    main_game.stage2_map.handle_move(frame_time)
    main_game.stage3_map.handle_move(frame_time)

    for Mon in main_game.stage1_monster:
        Mon.handle_move(frame_time)

    for Mon in main_game.stage2_monster:
        Mon.handle_move(frame_time)

    for Mon in main_game.stage3_monster:
        Mon.handle_move(frame_time)

    for ATK in main_game.stage2_monster_attack:
        if ATK.ATTACK == 1:
            ATK.attack_move(frame_time)
        else:
            ATK.handle_move(frame_time)

    for ATK in main_game.stage3_monster_attack:
        if ATK.ATTACK == 1:
            ATK.attack_move(frame_time)
        else:
            ATK.handle_move(frame_time)

    for Trp in main_game.stage2_trap:
        Trp.handle_move(frame_time)

    for PROTECT in main_game.protected:
        PROTECT.handle_move(frame_time)