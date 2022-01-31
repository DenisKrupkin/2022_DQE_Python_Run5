"""
Home task for Module 2 - Collections

Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""
import random  # Import of random for generation of random numbers and letters in dictionaries
import string  # Import of string for operations with keys of dictionaries

# Create a list of random number of dicts (from 2 to 10)
list_of_random_dictionaries = []  # Create empty list
for i in range(0, random.randint(2, 10)):  # FOR statement with randon number of iterations between 2 and 10
    sample_dictionary = {random.choice(string.ascii_lowercase): random.randint(0, 100)
                         for y in range(0, random.randint(0, 100))}  # Generation of random dictionary
    list_of_random_dictionaries.append(sample_dictionary)  # Adding of generated dictionary to list
print(f'List of random dictionaries: {list_of_random_dictionaries}.')  # Printing of final list

# Get previously generated list of dicts and create one common dict
final_dict = {}  # Create empty final dictionary
common_dict = {}  # Create empty temporary dictionary
dictionary_number = 0  # Variable for storing of dictionary number
for item in list_of_random_dictionaries:  # For each item in list with random dictionaries
    for key, value in item.items():  # Take key and value for each dictionary
        common_dict.update({key + f'_{dictionary_number}': value})  # Add key_dictionary_number:value to temp dictionary
    dictionary_number = dictionary_number + 1  # Increase dictionary_number
max_key = ""  # Empty variable for keys with maximum values
dict_a = {}  # Set of empty temporary dictionaries for each letter separately
temp_a = {}
dict_b = {}
temp_b = {}
dict_c = {}
temp_c = {}
dict_d = {}
temp_d = {}
dict_e = {}
temp_e = {}
dict_f = {}
temp_f = {}
dict_g = {}
temp_g = {}
dict_h = {}
temp_h = {}
dict_i = {}
temp_i = {}
dict_j = {}
temp_j = {}
dict_k = {}
temp_k = {}
dict_l = {}
temp_l = {}
dict_m = {}
temp_m = {}
dict_n = {}
temp_n = {}
dict_o = {}
temp_o = {}
dict_p = {}
temp_p = {}
dict_q = {}
temp_q = {}
dict_r = {}
temp_r = {}
dict_s = {}
temp_s = {}
dict_t = {}
temp_t = {}
dict_u = {}
temp_u = {}
dict_v = {}
temp_v = {}
dict_w = {}
temp_w = {}
dict_x = {}
temp_x = {}
dict_y = {}
temp_y = {}
dict_z = {}
temp_z = {}
for key, value in common_dict.items():  # Take key: value in temporary dictionary
    if key[0] == 'a':  # Check if first letter in key = 'a'
        temp_a = {}  # Clear inner temporary dictionary
        dict_a.update({key: value})  # Add key: value to second temp dictionary for 'a' keys
        if len(dict_a) > 1:  # Check if count of keys with 'a' are more than one
            v_a = list(dict_a.values())  # Define list for values
            k_a = list(dict_a.keys())  # Define list for keys
            max_key = k_a[v_a.index(max(v_a))]  # Find key with max value
            temp_a[max_key] = dict_a[max_key]  # Add key with max value to temp dictionary
        else:  # IF there is only one 'a' letter in all dictionaries
            v_a = dict_a[key]  # Take value by key
            k_a = list(dict_a.keys())  # Define list of keys
            new_key_a = k_a[0].partition('_')[0]  # Shrink 'a' key using partition. Delete all after first letter.
            temp_a.update({new_key_a: v_a})  # Add changed key with value to temp dictionary
    # Do the same for all others letters
    elif key[0] == 'b':
        temp_b = {}
        dict_b.update({key: value})
        if len(dict_b) > 1:
            v_b = list(dict_b.values())
            k_b = list(dict_b.keys())
            max_key = k_b[v_b.index(max(v_b))]
            temp_b[max_key] = dict_b[max_key]
        else:
            v_b = dict_b[key]
            k_b = list(dict_b.keys())
            new_key_b = k_b[0].partition('_')[0]
            temp_b.update({new_key_b: v_b})
    elif key[0] == 'c':
        temp_c = {}
        dict_c.update({key: value})
        if len(dict_c) > 1:
            v_c = list(dict_c.values())
            k_c = list(dict_c.keys())
            max_key = k_c[v_c.index(max(v_c))]
            temp_c[max_key] = dict_c[max_key]
        else:
            v_c = dict_c[key]
            k_c = list(dict_c.keys())
            new_key_c = k_c[0].partition('_')[0]
            temp_c.update({new_key_c: v_c})
    elif key[0] == 'd':
        temp_d = {}
        dict_d.update({key: value})
        if len(dict_d) > 1:
            v_d = list(dict_d.values())
            k_d = list(dict_d.keys())
            max_key = k_d[v_d.index(max(v_d))]
            temp_d[max_key] = dict_d[max_key]
        else:
            v_d = dict_d[key]
            k_d = list(dict_d.keys())
            new_key_d = k_d[0].partition('_')[0]
            temp_d.update({new_key_d: v_d})
    elif key[0] == 'e':
        temp_e = {}
        dict_e.update({key: value})
        if len(dict_e) > 1:
            v_e = list(dict_e.values())
            k_e = list(dict_e.keys())
            max_key = k_e[v_e.index(max(v_e))]
            temp_e[max_key] = dict_e[max_key]
        else:
            v_e = dict_e[key]
            k_e = list(dict_e.keys())
            new_key_e = k_e[0].partition('_')[0]
            temp_e.update({new_key_e: v_e})
    elif key[0] == 'f':
        temp_f = {}
        dict_f.update({key: value})
        if len(dict_f) > 1:
            v_f = list(dict_f.values())
            k_f = list(dict_f.keys())
            max_key = k_f[v_f.index(max(v_f))]
            temp_f[max_key] = dict_f[max_key]
        else:
            v_f = dict_f[key]
            k_f = list(dict_f.keys())
            new_key_f = k_f[0].partition('_')[0]
            temp_f.update({new_key_f: v_f})
    elif key[0] == 'g':
        temp_g = {}
        dict_g.update({key: value})
        if len(dict_g) > 1:
            v_g = list(dict_g.values())
            k_g = list(dict_g.keys())
            max_key = k_g[v_g.index(max(v_g))]
            temp_g[max_key] = dict_g[max_key]
        else:
            v_g = dict_g[key]
            k_g = list(dict_g.keys())
            new_key_g = k_g[0].partition('_')[0]
            temp_g.update({new_key_g: v_g})
    elif key[0] == 'h':
        temp_h = {}
        dict_h.update({key: value})
        if len(dict_h) > 1:
            v_h = list(dict_h.values())
            k_h = list(dict_h.keys())
            max_key = k_h[v_h.index(max(v_h))]
            temp_h[max_key] = dict_h[max_key]
        else:
            v_h = dict_h[key]
            k_h = list(dict_h.keys())
            new_key_h = k_h[0].partition('_')[0]
            temp_h.update({new_key_h: v_h})
    elif key[0] == 'i':
        temp_i = {}
        dict_i.update({key: value})
        if len(dict_i) > 1:
            v_i = list(dict_i.values())
            k_i = list(dict_i.keys())
            max_key = k_i[v_i.index(max(v_i))]
            temp_i[max_key] = dict_i[max_key]
        else:
            v_i = dict_i[key]
            k_i = list(dict_i.keys())
            new_key_i = k_i[0].partition('_')[0]
            temp_i.update({new_key_i: v_i})
    elif key[0] == 'j':
        temp_j = {}
        dict_j.update({key: value})
        if len(dict_j) > 1:
            v_j = list(dict_j.values())
            k_j = list(dict_j.keys())
            max_key = k_j[v_j.index(max(v_j))]
            temp_j[max_key] = dict_j[max_key]
        else:
            v_j = dict_j[key]
            k_j = list(dict_j.keys())
            new_key_j = k_j[0].partition('_')[0]
            temp_j.update({new_key_j: v_j})
    elif key[0] == 'k':
        temp_k = {}
        dict_k.update({key: value})
        if len(dict_k) > 1:
            v_k = list(dict_k.values())
            k_k = list(dict_k.keys())
            max_key = k_k[v_k.index(max(v_k))]
            temp_k[max_key] = dict_k[max_key]
        else:
            v_k = dict_k[key]
            k_k = list(dict_k.keys())
            new_key_k = k_k[0].partition('_')[0]
            temp_k.update({new_key_k: v_k})
    elif key[0] == 'l':
        temp_l = {}
        dict_l.update({key: value})
        if len(dict_l) > 1:
            v_l = list(dict_l.values())
            k_l = list(dict_l.keys())
            max_key = k_l[v_l.index(max(v_l))]
            temp_l[max_key] = dict_l[max_key]
        else:
            v_l = dict_l[key]
            k_l = list(dict_l.keys())
            new_key_l = k_l[0].partition('_')[0]
            temp_l.update({new_key_l: v_l})
    elif key[0] == 'm':
        temp_m = {}
        dict_m.update({key: value})
        if len(dict_m) > 1:
            v_m = list(dict_m.values())
            k_m = list(dict_m.keys())
            max_key = k_m[v_m.index(max(v_m))]
            temp_m[max_key] = dict_m[max_key]
        else:
            v_m = dict_m[key]
            k_m = list(dict_m.keys())
            new_key_m = k_m[0].partition('_')[0]
            temp_m.update({new_key_m: v_m})
    elif key[0] == 'n':
        temp_n = {}
        dict_n.update({key: value})
        if len(dict_n) > 1:
            v_n = list(dict_n.values())
            k_n = list(dict_n.keys())
            max_key = k_n[v_n.index(max(v_n))]
            temp_n[max_key] = dict_n[max_key]
        else:
            v_n = dict_n[key]
            k_n = list(dict_n.keys())
            new_key_n = k_n[0].partition('_')[0]
            temp_n.update({new_key_n: v_n})
    elif key[0] == 'o':
        temp_o = {}
        dict_o.update({key: value})
        if len(dict_o) > 1:
            v_o = list(dict_o.values())
            k_o = list(dict_o.keys())
            max_key = k_o[v_o.index(max(v_o))]
            temp_o[max_key] = dict_o[max_key]
        else:
            v_o = dict_o[key]
            k_o = list(dict_o.keys())
            new_key_o = k_o[0].partition('_')[0]
            temp_o.update({new_key_o: v_o})
    elif key[0] == 'p':
        temp_p = {}
        dict_p.update({key: value})
        if len(dict_p) > 1:
            v_p = list(dict_p.values())
            k_p = list(dict_p.keys())
            max_key = k_p[v_p.index(max(v_p))]
            temp_p[max_key] = dict_p[max_key]
        else:
            v_p = dict_p[key]
            k_p = list(dict_p.keys())
            new_key_p = k_p[0].partition('_')[0]
            temp_p.update({new_key_p: v_p})
    elif key[0] == 'q':
        temp_q = {}
        dict_q.update({key: value})
        if len(dict_q) > 1:
            v_q = list(dict_q.values())
            k_q = list(dict_q.keys())
            max_key = k_q[v_q.index(max(v_q))]
            temp_q[max_key] = dict_q[max_key]
        else:
            v_q = dict_q[key]
            k_q = list(dict_q.keys())
            new_key_q = k_q[0].partition('_')[0]
            temp_q.update({new_key_q: v_q})
    elif key[0] == 'r':
        temp_r = {}
        dict_r.update({key: value})
        if len(dict_r) > 1:
            v_r = list(dict_r.values())
            k_r = list(dict_r.keys())
            max_key = k_r[v_r.index(max(v_r))]
            temp_r[max_key] = dict_r[max_key]
        else:
            v_r = dict_r[key]
            k_r = list(dict_r.keys())
            new_key_r = k_r[0].partition('_')[0]
            temp_r.update({new_key_r: v_r})
    elif key[0] == 's':
        temp_s = {}
        dict_s.update({key: value})
        if len(dict_s) > 1:
            v_s = list(dict_s.values())
            k_s = list(dict_s.keys())
            max_key = k_s[v_s.index(max(v_s))]
            temp_s[max_key] = dict_s[max_key]
        else:
            v_s = dict_s[key]
            k_s = list(dict_s.keys())
            new_key_s = k_s[0].partition('_')[0]
            temp_s.update({new_key_s: v_s})
    elif key[0] == 't':
        temp_t = {}
        dict_t.update({key: value})
        if len(dict_t) > 1:
            v_t = list(dict_t.values())
            k_t = list(dict_t.keys())
            max_key = k_t[v_t.index(max(v_t))]
            temp_t[max_key] = dict_t[max_key]
        else:
            v_t = dict_t[key]
            k_t = list(dict_t.keys())
            new_key_t = k_t[0].partition('_')[0]
            temp_t.update({new_key_t: v_t})
    elif key[0] == 'u':
        temp_u = {}
        dict_u.update({key: value})
        if len(dict_u) > 1:
            v_u = list(dict_u.values())
            k_u = list(dict_u.keys())
            max_key = k_u[v_u.index(max(v_u))]
            temp_u[max_key] = dict_u[max_key]
        else:
            v_u = dict_u[key]
            k_u = list(dict_u.keys())
            new_key_u = k_u[0].partition('_')[0]
            temp_u.update({new_key_u: v_u})
    elif key[0] == 'v':
        temp_v = {}
        dict_v.update({key: value})
        if len(dict_v) > 1:
            v_v = list(dict_v.values())
            k_v = list(dict_v.keys())
            max_key = k_v[v_v.index(max(v_v))]
            temp_v[max_key] = dict_v[max_key]
        else:
            v_v = dict_v[key]
            k_v = list(dict_v.keys())
            new_key_v = k_v[0].partition('_')[0]
            temp_v.update({new_key_v: v_v})
    elif key[0] == 'w':
        temp_w = {}
        dict_w.update({key: value})
        if len(dict_w) > 1:
            v_w = list(dict_w.values())
            k_w = list(dict_w.keys())
            max_key = k_w[v_w.index(max(v_w))]
            temp_w[max_key] = dict_w[max_key]
        else:
            v_w = dict_w[key]
            k_w = list(dict_w.keys())
            new_key_w = k_w[0].partition('_')[0]
            temp_w.update({new_key_w: v_w})
    elif key[0] == 'x':
        temp_x = {}
        dict_x.update({key: value})
        if len(dict_x) > 1:
            v_x = list(dict_x.values())
            k_x = list(dict_x.keys())
            max_key = k_x[v_x.index(max(v_x))]
            temp_x[max_key] = dict_x[max_key]
        else:
            v_x = dict_x[key]
            k_x = list(dict_x.keys())
            new_key_x = k_x[0].partition('_')[0]
            temp_x.update({new_key_x: v_x})
    elif key[0] == 'y':
        temp_y = {}
        dict_y.update({key: value})
        if len(dict_y) > 1:
            v_y = list(dict_y.values())
            k_y = list(dict_y.keys())
            max_key = k_y[v_y.index(max(v_y))]
            temp_y[max_key] = dict_y[max_key]
        else:
            v_y = dict_y[key]
            k_y = list(dict_y.keys())
            new_key_y = k_y[0].partition('_')[0]
            temp_y.update({new_key_y: v_y})
    elif key[0] == 'z':
        temp_z = {}
        dict_z.update({key: value})
        if len(dict_z) > 1:
            v_z = list(dict_z.values())
            k_z = list(dict_z.keys())
            max_key = k_z[v_z.index(max(v_z))]
            temp_z[max_key] = dict_z[max_key]
        else:
            v_z = dict_z[key]
            k_z = list(dict_z.keys())
            new_key_z = k_z[0].partition('_')[0]
            temp_z.update({new_key_z: v_z})
final_dict.update(temp_a)  # Adding maximum key: value or single key: value for each letter to final dictionary
final_dict.update(temp_b)
final_dict.update(temp_c)
final_dict.update(temp_d)
final_dict.update(temp_e)
final_dict.update(temp_f)
final_dict.update(temp_g)
final_dict.update(temp_h)
final_dict.update(temp_i)
final_dict.update(temp_j)
final_dict.update(temp_k)
final_dict.update(temp_l)
final_dict.update(temp_m)
final_dict.update(temp_n)
final_dict.update(temp_o)
final_dict.update(temp_p)
final_dict.update(temp_q)
final_dict.update(temp_r)
final_dict.update(temp_s)
final_dict.update(temp_t)
final_dict.update(temp_u)
final_dict.update(temp_v)
final_dict.update(temp_w)
final_dict.update(temp_x)
final_dict.update(temp_y)
final_dict.update(temp_z)
print(f'Final dictionary:{final_dict}')  # Printing of final dictionary
