# cli.py

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="rpchecker", description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",)
        
    return parser.parse_args()

#==============================================================================================
    
def display_check_result(result, url, error=""):
    """Mostra o resultado de um teste de resultado."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"O pai tá on!"')
    else:
        print(f'"Deixa baixo, tá off" \n  Erro: "{error}"') 
        
