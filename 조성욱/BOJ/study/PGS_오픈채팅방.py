def solution(record):
    answer = []

    dict = {}
    answer_ = []

    for r in record:
        record_ = list(map(str, r.split()))
        if record_[0] == 'Enter':
            dict[record_[1]] = record_[2] + '님이'
            answer_.append([record_[1], '들어왔습니다.'])
        elif record_[0] == 'Leave':
            answer_.append([record_[1], '나갔습니다.'])
        else:
            dict[record_[1]] = record_[2] + '님이'


    for i in answer:
        answer.append(dict[i[0]]+' '+i[1])



    return answer