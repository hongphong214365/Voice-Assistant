import json
import traceback
from config import LANG, DEBUG


def handle_config_error(
    filename: str,
    feature: str,
    error: Exception,
) -> None:
    if isinstance(error, json.JSONDecodeError):
        if LANG.startswith("vi"):
            print(
                f'lỗi: File JSON "{filename}" không hợp lệ.\n'
                f"Vị trí: Dòng {error.lineno}, cột {error.colno}\n"
                f"Chi tiết: {error.msg}\n\n"
                "Tính năng liên quan do lỗi trên nên tạm thời bị vô hiệu hóa.\n"
                "Để tính năng hoạt động, bạn vui lòng sửa lại file JSON "
                "và khởi động lại bot."
            )
        else:
            print(
                f'Error: JSON file "{filename}" is invalid.\n'
                f"Location: line {error.lineno}, column {error.colno}.\n"
                f"Details: {error.msg}\n\n"
                "The related feature has been temporarily disabled بسبب this error.\n"
                "To enable the feature, please fix the JSON file and restart the bot."
            )

    elif isinstance(error, FileNotFoundError):
        if LANG.startswith("vi"):
            print(
                f'Lỗi: Không tìm thấy file JSON "{filename}".\n\n'
                f"Tính năng {feature} do lỗi trên nên tạm thời "
                "bị vô hiệu hóa.\n"
                "Để tính năng hoạt động, bạn vui lòng khôi phục "
                "file JSON và khởi động lại bot."
            )
        else:
            print(
                f'Error: JSON file "{filename}" was not found.\n\n'
                f"The {feature} feature has been temporarily disabled "
                "due to this error.\n"
                "To enable it, please restore the JSON file and restart the bot."
            )
    if DEBUG:
        traceback.print_exc()
