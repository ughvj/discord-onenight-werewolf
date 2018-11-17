import random

class Master():

    def __init__(self, players, jobs):
        # deal
        for i, player in enumerate(players):
            random.shuffle(jobs)
            player.Ibecome(jobs.pop(-1))

        self.players = players
        self.jobs = jobs

        # for seer
        tmp = ''
        for job in self.jobs:
            if not job.usingSomeone():
                tmp += job.getDisplayName() + ' '
        self.nouse_display = tmp

        # for werewolf
        tmp = []
        for player in self.players:
            if player.Iam().amIWerewolf():
                tmp.append(player)
        self.werewolfs_list = tmp

        # for thief
        self.thief_exchange_actor = None
        self.thief_exchange_target = None

    def nightFalls(self, player):
        ret = ':first_quarter_moon_with_face: あなたは%sです' % player.Iam().getDisplayName()
        # 人狼の仲間認識
        if player.Iam().amIWerewolf():
            friend_name = ' '
            for friend in self.werewolfs_list:
                if not player.getName() == friend.getName():
                    friend_name += friend.getName() + ' '
            if friend_name == ' ':
                ret += ' 味方は居ません '
            else:
                ret += ' 味方は%sです' % friend_name

        if player.Iam().getName() == 'seer':
            ret += ' アクションの対象を`/act [対象ID]`で指定してください 使われていない役職を占うには、`/act`してください'
        elif player.Iam().getName() == 'thief':
            ret += ' アクションの対象を`/act [対象ID]`で指定してください'
        else:
            ret += ' 準備ができたら`/act`してください。'
        return ret

    def sunrise(self):
        # 怪盗の処理
        if not self.thief_exchange_target == None:
            tmp = self.thief_exchange_actor.Iam()
            self.thief_exchange_actor.Ibecome(self.thief_exchange_target.Iam())
            self.thief_exchange_target.Ibecome(tmp)
        return ':sun_with_face: 夜が明けました `/vote [対象ID]`で投票します プレイヤーの一覧は`/getp`で確認できます'

    def act(self, actor, target):
        for player in self.players:
            if actor == player.getName():
                if target >= len(self.players):
                    return ':exclamation: 対象が存在しません'
                # 行動済みのとき
                if player.haveIActed():
                    return ':exclamation: 既に行動済みです'
                player.actedPlayer()
                # 占い師のアクション
                if player.Iam().getName() == 'seer':
                    if not target == -1:
                        player.actedPlayer()
                        return ':white_check_mark: %sは%sです' % (self.players[target].getName(), self.players[target].Iam().getDisplayName())
                    else:
                        player.actedPlayer()
                        return ':white_check_mark: 使われていない職業は%sです' % self.nouse_display
                # 怪盗のアクション
                elif player.Iam().getName() == 'thief':
                    self.thief_exchange_actor = player
                    self.thief_exchange_target = self.players[target]
                    player.actedPlayer()
                    return ':white_check_mark: %sと役職を交換し、%sになりました' % (self.players[target].getName(), self.players[target].Iam().getDisplayName())

                # そのほかのアクション
                else:
                    return ':white_check_mark: 準備が完了しました 他のプレイヤーの行動をお待ちください'

    def vote(self, actor, target):
        for player in self.players:
            if actor == player.getName():
                if player.haveIVoted():
                    return ':exclamation: 既に投票済みです'
                if target >= len(self.players):
                    return ':exclamation: 対象が存在しません'
                if self.players[target].getName() == player.getName():
                    return ':exclamation: 自分には投票できません'
                self.players[target].someoneWasVoted()
                player.IVotedThisPlayer(self.players[target].getName())
                player.votedPlayer()
        return ':white_check_mark: %sに投票しました 他のプレイヤーの投票をお待ちください' % self.players[target].getName()

    def gameset(self):
        # 最大票数を確認する
        max_vote = 1
        for player in self.players:
            if player.howMuchIWasVoted() > max_vote:
                max_vote = player.howMuchIWasVoted()

        # 勝利判定
        winner = '人狼'
        for player in self.players:
            if player.howMuchIWasVoted() == max_vote:
                if player.Iam().amIWerewolf():
                    winner = '村人'
                if player.Iam().getName() == 'suisider':
                    winner = '吊人'
                    break

        ret = ':arrow_down:結果:arrow_down:\n'
        # 結果表作成
        for player in self.players:
            j = player.Iam().getName()
            if winner == '人狼':
                if j == 'werewolf' or j == 'madman':
                    ret += ':o: '
                else:
                    ret += ':x: '
            if winner == '村人':
                if j == 'werewolf' or j == 'madman':
                    ret += ':x: '
                else:
                    ret += ':o: '
            if winner == '吊人':
                if j == 'suisider':
                    ret += ':o: '
                else:
                    ret += ':x: '

            if player.howMuchIWasVoted() == max_vote:
                ret += ':skull: '
            else:
                ret += ':neutral_face: '

            ret += '__**' + player.getName() + '**__: '
            ret += player.Iam().getDisplayName() + ' '
            ret += '  '
            ret += ':point_right: ' + player.whomDidIVoted() + ' '
            ret += '\n'

        ret += ':no_pedestrians: ' + self.nouse_display + '\n'

        return ret

    def haveAllPlayerActed(self):
        for player in self.players:
            if not player.haveIActed():
                return False
        return True

    def haveAllPlayerVoted(self):
        for player in self.players:
            if not player.haveIVoted():
                return False
        return True
