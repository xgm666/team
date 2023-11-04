if __name__ == "__main__":
    import_button = tk.Button(root, text="Import Excel", command=import_excel_button)
    import_button.pack()

    create_notification_button = tk.Button(root, text="Create Notification", command=create_notification_button)
    create_notification_button.pack()

    send_notifications_button = tk.Button(root, text="Send Notifications", command=send_notifications_button)
    send_notifications_button.pack()

    root.mainloop()