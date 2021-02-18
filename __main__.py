from PySide2 import QtWidgets, QtGui
import socket
import server  # DON`T REMOVE


def save_file_data(chunks: dict) -> None:
    keys = sorted(chunks)
    bytes_data = b''
    for key in keys:
        value = chunks.get(key)
        bytes_data += value
    with open('test.jpg', 'wb') as f:
        f.write(bytes_data)


def client():
    chunks = {}
    HOST = '127.0.0.1'
    PORT = 8888
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message_next = "next"
            s.send(message_next.encode())
            data = s.recv(2048)
            if data:
                chunks[data[0]] = data[1:]
            else:
                break
    save_file_data(chunks)
    path_to_image = "test.jpg"
    return path_to_image


def main():
    path = client()
    app = QtWidgets.QApplication([])
    label = QtWidgets.QLabel()
    label.setMinimumSize(100, 100)
    label.setPixmap(QtGui.QPixmap(path))
    label.show()
    app.exec_()


if __name__ == '__main__':
    main()
