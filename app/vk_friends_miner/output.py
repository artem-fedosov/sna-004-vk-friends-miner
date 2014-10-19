from StringIO import StringIO

def _to_str(obj):
    if isinstance(obj, unicode):
        obj = obj.encode('utf-8')
    return '"%s"' % obj if type(obj) == str else str(obj)


def to_glm(users_data, friendship_data, filename=None):
    friends_set = set(friendship_data.keys())
    edges_set = {
        (max(source, target), min(source, target))
        for source in friendship_data
        for target in friendship_data[source] if target in friends_set  # exclude unknown persons
    }

    lines = ['graph', '[ directed 0']

    for data in users_data:
        lines.append('\tnode [')
        lines.append('\t\tid %s' % data['uid'])
        lines.append('\t\tlabel %s' % _to_str(data['last_name'] + ' ' + data['first_name']))
        for key, value in sorted(data.iteritems()):
            if key in [u'uid', u'user_id']:
                continue
            lines.append('\t\t%s %s' % (key.encode('utf-8'), _to_str(value)))
        lines.append('\t]')

    for source, target in edges_set:
        lines.append('\tedge [')
        lines.append('\t\tsource %s' % source)
        lines.append('\t\ttarget %s' % target)
        lines.append('\t]')
    lines.append(']')
    lines = [line + '\n' for line in lines]

    if filename:
        with open(filename, 'w') as glm_file:
            glm_file.writelines(lines)
    else:
        s = StringIO()
        s.writelines(lines)
        s.seek(0)
        return s

__all__ = ['to_glm']