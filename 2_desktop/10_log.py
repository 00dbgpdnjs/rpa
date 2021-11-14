import logging # logging : 로그를 남김

# 1. Leave a log at the terminal.

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# # 1st arg: 디버그 레벨 이상의 모든 로그를 찍어줌  
# # 2nd arg: 시간(로그가 언제 찍혔는지), 로그의 레벨,  로그 내용
# # level : debug < info < warning < error < critical

# # Types of logging.
# logging.debug("아 이거 누가 짠거야~~") # debug : Developer's comment.
# logging.info("자동화 수행 준비") # 방문자의 pc에도 보임
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는 ...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다...")


# 2. Leave a log on the also file at the same time.

from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger() # Get logger
logger.setLevel(logging.DEBUG)

# 스트림[터미널]에 로그 출력
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20201010141011.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# Which log will you leave
logger.debug("로그를 남겨보는 테스크를 진행합니다.")