# TODO 1: 채팅방에 누군가 들어오면 다음 메시지가 출력된다. "[닉네임]님이 들어왔습니다."
# TODO 2: 채팅방에서 누군가 나가면 다음 메시지가 출력된다. "[닉네임]님이 나갔습니다."
# TODO 3: 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
#  채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
#  채팅방에서 닉네임을 변경한다.
# TODO 4 : 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
# TODO 5 :채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
#  모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를
#  문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
# # herf = https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3

RECORD = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
user_data = {}


def chat_output(user_log):
    output_string = ""
    return output_string


def enter_chat(user_log):
    '''유저 아이디를 인식해서 출력해줌.'''

    data_split = user_log.split()

    user_id = data_split[1]
    user_name = data_split[2]

    user_data[f"{user_id}"] = user_name
    string_print = f"{user_data[f'{user_id}']}님이 들어왔습니다."

    return string_print


def out_chat(user_log):
    data_split = user_log.split()

    user_id = data_split[1]
    user_name = data_split[2]


def change_chat(user_log):
    data_split = user_log.split()

    user_id = data_split[1]
    user_name = data_split[2]



def solution(record):
    answer = []
    for r in record:
        if "Enter" in r:
            enter_chat(r)
        elif "Leave" in r:
            out_chat(r)
        elif "Change" in r:
            change_chat(r)
    print(f"user_data: {user_data}\n\n")
    return answer


print(solution(RECORD))

