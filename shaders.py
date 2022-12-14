
from myLibrary import *


def flat(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = dotProduct(triangleNormal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def gourad(render, **kwargs):
    # Iluminacion por vertice, se interpola
    # la iluminacion por cada pixel

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensityA = dotProduct(nA, dirLight)
    intensityB = dotProduct(nB, dirLight)
    intensityC = dotProduct(nC, dirLight)

    intensity = intensityA * u + intensityB * v + intensityC * w
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def phong(render, **kwargs):
    # Iluminacion por pixel

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = dotProduct(normal, dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b


def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = dotProduct(normal, dirLight)

    if intensity > 0.7:
        intensity = 1
    elif intensity > 0.3:
        intensity = 0.5
    else:
        intensity = 0.05

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def textureBlend(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensity = dotProduct(normal, dirLight)

    if intensity < 0:
        intensity = 0

    b *= intensity
    g *= intensity
    r *= intensity

    if render.active_texture2:
        texColor = render.active_texture2.getColor(tx, ty)
        b += (texColor[0] / 255) * (1 - intensity)
        g += (texColor[1] / 255) * (1 - intensity)
        r += (texColor[2] / 255) * (1 - intensity)

    return r, g, b


def shader1(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensityA = dotProduct(nA, dirLight)
    intensityB = dotProduct(nB, dirLight)
    intensityC = dotProduct(nC, dirLight)

    intensity = intensityA * u + intensityB * v + intensityC * w
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0.5:
        return r, g, b
    else:
        return 0, 0, 0


def holographic(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255
    r = 1-r
    g = 1-g
    b = 1-b

    return r, g, b


def colors(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    dirLight = [-render.directional_light[0],
                -render.directional_light[1],
                -render.directional_light[2]]
    intensityA = dotProduct(nA, dirLight)
    intensityB = dotProduct(nB, dirLight)
    intensityC = dotProduct(nC, dirLight)

    intensity = intensityA * u + intensityB * v + intensityC * w

    if intensity >= 0.5:
        r = r**r
        g = 0
        b = 0

    if (intensity > 0.3) and (intensity < 0.5):
        r = r**r
        g = g**g
        b = 0

    if intensity < 0.3:
        r = 0
        g = 0
        b = b**b

    return r, g, b


def normalMap(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w
    normal = (nX, nY, nZ)

    dirLight = [render.directional_light]

    if render.normal_map:
        texNormal = render.normal_map.getColor(tx, ty)
        texNormal = [(texNormal[2] / 255) * 2 - 1,
                     (texNormal[1] / 255) * 2 - 1,
                     (texNormal[0] / 255) * 2 - 1]

        texNormal = texNormal / np.linalg.norm(texNormal)

        edge1 = subtract(B, A)
        edge2 = subtract(C, A)
        deltaUV1 = subtract(tB, tA)
        deltaUV2 = subtract(tC, tA)

        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])

        tangent = [f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0]),
                   f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1]),
                   f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])]
        tangent = normalize(tangent)
        tangent = subtract(tangent, multiplyMatrices(
            dotProduct(tangent, normal), normal))
        tangent = normalize(tangent)

        bitangent = crossProduct(normal, tangent)
        bitangent = normalize(bitangent)

        tangentMatrix = [[tangent[0],  bitangent[0],  normal[0]],
                         [tangent[1],  bitangent[1],  normal[1]],
                         [tangent[2],  bitangent[2],  normal[2]]]

        texNormal = tangentMatrix @ texNormal
        texNormal = texNormal.tolist()[0]
        texNormal = normalize(texNormal)
        intensity = dotProduct(texNormal, -dirLight)
    else:
        intensity = dotProduct(normal, -dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0
