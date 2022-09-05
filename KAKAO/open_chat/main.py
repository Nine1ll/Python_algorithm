# TODO 3: 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
#  채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
#  채팅방에서 닉네임을 변경한다.
# TODO 4 : 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
# TODO 5 :채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
#  모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를
#  문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
# # herf = https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3


RECORDS = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
log_data = {}


def chat_output(user_log):
    output_string = ""
    return output_string


def enter_chat(user_log):
    '''유저가 채팅방에 들어왔을 때, 아이디를 인식해서 들어왔다고 출력해줌.'''

    data_split = user_log.split()

    user_id = data_split[1]
    user_name = data_split[2]
    if user_id in log_data.keys() and user_name != log_data[user_id]: # 유저 로그에 id가 존재하지만, 이름이 다르면 -> log_data 안에 있는 이름 교체
        pass
    log_data[f"{user_id}"] = user_name
    string_print = f"{log_data[f'{user_id}']}님이 들어왔습니다."

    return string_print


def out_chat(user_log):
    '''유저가 채팅방에 들어왔을 때, 아이디를 인식해서 나갔다고 출력해줌.'''
    data_split = user_log.split()

    user_id = data_split[1]

    string_print = f"{log_data[f'{user_id}']}님이 나갔습니다."

    return string_print


def change_chat(user_log):
    data_split = user_log.split()

    user_id = data_split[1]
    user_name = data_split[2]

    log_data[f"{user_id}"] = user_name


def solution(record):
    answer = []
    for r in record:
        if "Enter" in r:
            answer.append(enter_chat(r))
        elif "Leave" in r:
            answer.append(out_chat(r))
        elif "Change" in r:
            change_chat(r)
    print(f"user_data: {log_data}\n\n")

    return answer


print(f"Record : {solution(RECORDS)}")

# "Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."