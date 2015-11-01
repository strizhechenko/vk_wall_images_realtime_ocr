#!/usr/bin/python

import json, urllib, time

wall_post_count_prev = 6825
group_id = "46074357"
have_pinned_post = True
request_interval = 1

index = have_pinned_post and 1 or 2
wall_get_url = 'https://api.vk.com/method/wall.get?owner_id=-' + group_id + '&count=' + str(index)


def wall_post_fetch():
    data = urllib.urlopen(wall_get_url).read()
    posts = json.loads(data)
    return posts.get('response')


def wall_post_print_image_links(response):
    for item in response[index:]:
        attachments = item.get('attachments')
        if not attachments:
            continue
        for attachment in attachments:
            photo = attachment.get('photo')
            if not photo:
                continue
            print photo.get('src_big')

while True:
    response = wall_post_fetch()
    wall_post_count = response[0]
    if wall_post_count == wall_post_count_prev:
        time.sleep(request_interval)
        continue
    wall_post_count_prev = wall_post_count
    wall_post_print_image_links(response)

