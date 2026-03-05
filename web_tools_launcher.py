import os
import subprocess
import sys


TOOLS = [
    {"id": "1", "name": "问卷定量交叉分析", "script": "问卷定量分析工具 v1.py"},
    {"id": "2", "name": "满意度全流程诊断", "script": "multi_regression_v1.1.py"},
    {"id": "3", "name": "满意度 IPA 相关性", "script": "relation_analysis.py"},
    {"id": "4", "name": "游戏体验全链路分析", "script": "game_analyst.py"},
    {"id": "5", "name": "问卷文本分析工具", "script": "问卷文本分析工具 v1.py"},
]


def run_tool(choice):
    tool = next((t for t in TOOLS if t["id"] == choice), None)
    if not tool:
        return False
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, tool["script"])
    if not os.path.exists(script_path):
        print(f"未找到脚本文件: {script_path}")
        return True
    cmd = [sys.executable, "-m", "streamlit", "run", script_path]
    subprocess.run(cmd)
    return True


def main():
    while True:
        print()
        print("==== 问卷 Web 工具启动菜单 ====")
        for t in TOOLS:
            print(f'{t["id"]}. {t["name"]}')
        print("0. 退出")
        choice = input("请输入要启动的工具序号并回车: ").strip()
        if choice == "0":
            break
        if not run_tool(choice):
            print("无效选择，请重试。")


if __name__ == "__main__":
    main()

