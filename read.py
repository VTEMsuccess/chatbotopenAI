import openai
import PyPDF2

openai.api_key = "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"

def reply_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1000,
        temperature=0.5,
        n=2,
        stop=None
    )

    return response.choices[0].text.strip()

import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        pdf_content = ''

        for page in reader.pages:
            pdf_content += page.extract_text()

        return pdf_content



def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


print("Chào mừng bạn đến với Chatbot Tra cứu Nghiên cứu và Kiến thức! Bạn cần giúp gì hôm nay?")
print("Để kết thúc, chỉ cần gõ 'bye'.")
print("nhấn read để chuyển đến nhập file PDF")

while True:
    user_input = input("Người dùng: ")
    if user_input.lower() == "bye":
        print("Chatbot: Hẹn gặp lại!")
        break
    elif user_input.lower() == "read":
        file_path = input("Nhập đường dẫn tới tập tin PDF: ")
        content = read_pdf(file_path)
        print("Chatbot: Nội dung tập tin:\n" + content)
    elif user_input.lower() == "write":
        file_path = input("Nhập đường dẫn tới tập tin: ")
        content = input("Nhập nội dung để ghi: ")
        write_to_file(file_path, content)
        print("Chatbot: Nội dung đã được ghi vào tập tin.")
    else:
        response = reply_response(user_input)
        print("Chatbot: " + response)
