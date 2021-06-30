from code_challenges.hashtable.hashtable import Hashtable

def hashmap_left_join(ht1, ht2):
    answer = []

    for bucket in ht1._bucket:
        if bucket:
            current = bucket.head
            while current:
                current_key = current.data[0]
                current_value = current.data[1]
                pairs = [current_key, current_value]

                if ht2.contains(current_key):
                    pairs.append(ht2.get(current_key))

                else:
                    pairs.append(None)

                answer.append(pairs)
                current = current.next

    return answer
