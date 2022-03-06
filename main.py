import user_input as ui
import task_logic as tl


def main():
    while True:
        print("(1) Use K=10  M=4 | (2)Enter K and M ")

        try:
            tmp = input()
            tmp = int(tmp)
            if tmp != 1 and tmp != 2:
                raise Exception("Enter (1) or (2)")
            else:
                if tmp == 1:
                    text = ui.i_text()
                    tl.get_top_k(10, 4, text)
                    break
                else:
                    k = ui.i_k()
                    m = ui.i_m()
                    text = ui.i_text()
                    tl.get_top_k(k, m, text)
                    break
        except ValueError:
            print("Incorrect value")
            break
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    main()
