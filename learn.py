def list_benefits() -> list[str]:
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
def build_sentence(info) -> str:
    return f"{info} is a benefit of functions"

#run the functions
print(",".join(list_benefits()))
print(build_sentence(list_benefits()[0]))