print("\n".join([('-'*(i)) + '*' +('-'*(10-(i))) if i<10 else ('-'*(10-(i%10))) + '*' +('-'*(i%10)) for i in range(20)])) 