import requests
import argparse
import hashlib


def login(username, password):
    password = '{MD5_HEX}' + hashlib.md5(password.encode('utf-8')).hexdigest()
    r = requests.post('http://net.tsinghua.edu.cn/do_login.php',
                      data={'action': 'login', 'username': username, 'password': password, 'ac_id': 1})
    print(r.text)
    print('')
    status()


def logout():
    r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data={'action': 'logout'})
    print(r.text)


def status():
    r = requests.post('http://net.tsinghua.edu.cn/rad_user_info.php')
    if len(r.text) == 0:
        print('not login')
        return
    status_arr = r.text.split(',')
    username = status_arr[0]
    online_time = int(status_arr[2]) - int(status_arr[1])
    ip = status_arr[8]
    flux_usage = int(status_arr[6])
    print("user: %s" % username)
    print("ip: %s" % ip)
    print("online time: %s" % format_time(online_time))
    print("flux usage: %s" % format_byte(flux_usage))


def format_time(sec):
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 3600 % 60
    return '%02d:%02d:%02d' % (h, m, s)


def format_byte(n):
    if n > 1e9:
        return "%.2fG" % (n / 1e9)
    elif n > 1e6:
        return "%.2fM" % (n / 1e6)
    elif n > 1e3:
        return "%.2fK" % (n / 1e3)
    else:
        return "%.2fB" % n


def main():
    parser = argparse.ArgumentParser(description='Connection tool for Tsinghua')
    parser.add_argument('action', help='login / logout / status')
    parser.add_argument('--username', '-u')
    parser.add_argument('--password', '-p')
    args = parser.parse_args()
    if args.action == 'login':
        if args.username is None or len(args.username) == 0:
            print('username cannot be empty')
            return
        if args.password is None or len(args.password) == 0:
            print('password cannot be empty')
            return
        login(args.username, args.password)
    elif args.action == 'logout':
        logout()
    elif args.action == 'status':
        status()


if __name__ == '__main__':
    main()
