import sys
import os

file_path = "/home/wrd/zjucad/libwetcloth/assets/general_examples/yarn_small_proto.xml"

pre_point_contents = []
post_point_contents = []
all_points = []
points = []
with open(file_path, "r") as f:
    for line in f:
        if line.startswith("<particle"):
            points.append(line)
            break
        else:
            pre_point_contents.append(line)

    for line in f:
        if line.startswith("<particle"):
            points.append(line)
        elif line.strip() == "":
            all_points.append(points)
            points = []
        else:
            post_point_contents.append(line)

n = 100
ofs1 = 10
width1 = 10
ofs2 = 20
# width2=98-ofs2

for i in range(ofs1, ofs1 + width1):
    for j in range(ofs2, 98 - ofs2):
        indices1 = [i, 98 - i]
        indices2 = [j]
        for k in indices1:
            for l in indices2:
                group_id = 10 if i == k else 11
                all_points[k][l] = all_points[k][l].replace('fixed="0"', 'fixed="1"')
                all_points[k][l] = all_points[k][l].replace(
                    f'group="0"', 'group="' + str(group_id) + '"'
                )
                all_points[l + 98][k] = all_points[l + 98][k].replace(
                    'fixed="0"', 'fixed="1"'
                )
                all_points[l + 98][k] = all_points[l + 98][k].replace(
                    f'group="1"', 'group="' + str(group_id) + '"'
                )


output_filepath = (
    "/home/wrd/zjucad/libwetcloth/assets/general_examples/yarn_small_bc1.xml"
)
with open(output_filepath, "w") as f:
    for line in pre_point_contents:
        f.write(line)

    f.write("\n")
    f.write(
        '<script type="translate" x="0.0" y="0.0" z="-2" w="0.0" start="0.0" end="0.2" group="10"/>\n'
    )
    f.write(
        '<script type="translate" x="0.0" y="0.0" z="2" w="0.0" start="0.0" end="0.2" group="11"/>\n'
    )
    f.write("\n")
    
    for points in all_points:
        for point in points:
            f.write(point)

    f.write("\n")
    for line in post_point_contents:
        f.write(line)
    f.write("\n")
