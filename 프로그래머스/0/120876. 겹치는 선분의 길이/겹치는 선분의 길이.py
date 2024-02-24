def solution(lines):
    all_lines = [set(range(min(l), max(l))) for l in lines]
    
    return len(all_lines[0] & all_lines[1] | all_lines[0] & all_lines[2] | all_lines[1] & all_lines[2])