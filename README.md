# Lahtp_advance_assigment_1

# 🛠 Networking Toolkit by Kavin

This repository contains **five Python networking tools** for learning and practicing socket programming. Each tool demonstrates core networking concepts using TCP, UDP, and multithreading.

---

## 📌 Tools Included

### 1. 🔍 **Port Scanner**

* Checks which ports are **open** on a target host.
* Uses **multi-threading** for faster scanning.
* Example use case: find open services on a server.

**Run:**

```bash
python port_scanner.py
```

You’ll be prompted to enter:

* Target domain/IP
* Port range to scan

---

### 2. 🏷 **Banner Grabber**

* Connects to an open port and **retrieves service information** (banner).
* Helps identify the running service/software version.
* Example: grabbing HTTP response headers from a web server.

**Run:**

```bash
python banner_grabber.py
```

---

### 3. 🔗 **TCP Client/Server**

* Demonstrates **basic TCP communication**.
* Client sends a message, server replies.
* Good starting point for understanding TCP sockets.

**Run Server:**

```bash
python tcp_server.py
```

**Run Client:**

```bash
python tcp_client.py
```

---

### 4. 📡 **UDP Client/Server**

* Demonstrates **basic UDP communication**.
* Uses `sendto()` and `recvfrom()` instead of TCP’s `send/recv`.
* Lightweight and connectionless.

**Run Server:**

```bash
python udp_server.py
```

**Run Client:**

```bash
python udp_client.py
```

---

### 5. 💬 **Chat Application**

* A simple **multi-client chat server** using TCP.
* Clients can:

  * `join` → Register with a nickname
  * `msg` → Send messages to everyone
  * `quit` → Leave the chat
* Uses **multithreading** to handle multiple clients simultaneously.

**Run Server:**

```bash
python chat_server.py
```

**Run Client:**

```bash
python chat_client.py
```

---

## ⚙️ Requirements

* Python 3.7+
* [`pyfiglet`](https://pypi.org/project/pyfiglet/) for ASCII banners

Install with:

```bash
pip install pyfiglet
```

---

## 📖 Learning Outcomes

By exploring these tools, you will learn:
✅ Socket creation and binding
✅ Difference between **TCP vs UDP**
✅ How to send and receive data over sockets
✅ Using **threads** for concurrent connections
✅ Building simple networking utilities

---

## ⚠️ Disclaimer

This toolkit is made **for educational purposes only**.
Do not use it against systems you don’t own or have permission to test.

---

## 👨‍💻 Author

**Kavin** – Networking & Python Enthusiast 🚀


