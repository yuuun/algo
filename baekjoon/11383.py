n, m = map(int, input().split())
images = [input() for _ in range(n)]
zipped_images = [input() for _ in range(n)]

for img, zimg in zip(images, zipped_images):
    for i in range(len(img)):
        if img[i] == zimg[i * 2] and img[i] == zimg[2 * i + 1]:
            continue
        print('Not Eyfa')
        exit()

print('Eyfa')