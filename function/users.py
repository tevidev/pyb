

owners = ["6094779754","5734114291"]  # Add owner ids here

def getUsersCount(filename) :
        if(file_exists(filename)) :
                lines = file(filename)
                return count(lines)
            } else :
                    return 0 # Return 0 if the file doesn't exist
    
    update = json_decode(file_get_contents('php:#input'), True)
    
    if (isset(update['message']['text'])) :
            message = update['message']['text']
            chat_id = update['message']['chat']['id']
        
            if (message === '/users') :
                    if (in_[chat_id, owners]) :
                            freeUserCount = getUsersCount('Database/free.txt')
                            paidUserCount = getUsersCount('Database/paid.txt')
                            banUserCount = getUsersCount('Database/banned.txt')
                            response = "<b>[×] Total users: {freeUserCount}%0A[×] Paid users: {paidUserCount}%0A[×] Banned users: {banUserCount}%0A%0A[×] Bot by: @OmenXD_Bins </b>"
                        } else :
                                response = "<b>𝙊𝙊𝙋𝙎! 𝙔𝙊𝙐 𝘼𝙍𝙀 𝙉𝙊𝙏 𝘼𝙉 𝘼𝘿𝙈𝙄𝙉  ❌</b>"
                        sendMessage(chat_id, response, message_id)
        