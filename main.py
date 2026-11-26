import os

ANSWER = "StallMail: for lazy agents guarding a Shopify store selling only heated socks, it answers 2 a.m. refund emails with 'checking the warehouse,' bills the owner $4 a stall, and lets the agent sleep."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ANSWER)


if __name__ == "__main__":
    main()
