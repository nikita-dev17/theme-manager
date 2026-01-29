from utils.files import create_dirs
from utils.theme import apply_theme


def menu():
    while True:
        popa = ["autumn", "blossom", "cozynight", "crimsonveil", "lanternia", "retrosunset", "sakuracat", "sakuraway"]
        try:
            choice = int(input("-------- Chose Theme --------\n"
                               "| <| 0 |> ---> exit         |\n"
                               "| <| 1 |> ---> autumn       |\n"
                               "| <| 2 |> ---> blossom      |\n"
                               "| <| 3 |> ---> cozynight    |\n"
                               "| <| 4 |> ---> crimsonveil  |\n"
                               "| <| 5 |> ---> lanternia    |\n"
                               "| <| 6 |> ---> retrosunset  |\n"
                               "| <| 7 |> ---> sakuracat    |\n"
                               "| <| 8 |> ---> sakuraway    |\n"
                               "-----------------------------\n--> "))
            if (choice >= 1) and (choice <= 10):
                return popa[choice - 1]
            elif choice == 0:
                exit()
            else:
                print("Wrong choice!!")
        except ValueError:
            print("Wrong choice!!")

        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    create_dirs()
    theme = menu()
    print(f"[INFO] Applying theme: {theme.upper()}")
    apply_theme(theme)
