# Copyright 2020 Alex Woroschilow <alex.woroschilow@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2,
# or (at your option) any later version, as published by the Free
# Software Foundation
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
pkgname="DeepinV20White"
pkgver="1.0"
pkgrel=`date +"%Y%m%d%H%M"`
epoch=
pkgdesc="DeepinV20 white KDE Theme"
arch=("x86_64")
url=""
license=("GPL")
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=()
noextract=()
md5sums=()
validpgpkeys=()

prepare() {
	pwd
}

build() {
    pwd
}

check() {
    pwd
}

package() {
	PWD=`pwd`

	DIR_AURORAE="${pkgdir}/usr/share/aurorae/themes"
	DIR_SCHEMES="${pkgdir}/usr/share/color-schemes"
	DIR_PLASMA="${pkgdir}/usr/share/plasma/desktoptheme"
	DIR_LAYOUT="${pkgdir}/usr/share/plasma/layout-templates"
	DIR_LOOKFEEL="${pkgdir}/usr/share/plasma/look-and-feel"
	DIR_WALLPAPER="${pkgdir}/usr/share/wallpapers"
	DIR_KVANTUM="${pkgdir}/usr/share/Kvantum"
	DIR_SDDM="${pkgdir}/usr/share/sddm/themes"
	DIR_ICONS="${pkgdir}/usr/share/icons"
	DIR_THEMES="${pkgdir}/usr/share/themes"

	install -d ${DIR_AURORAE}
	install -d ${DIR_SCHEMES}
	install -d ${DIR_PLASMA}
	install -d ${DIR_LAYOUT}
	install -d ${DIR_LOOKFEEL}
	install -d ${DIR_WALLPAPER}
	install -d ${DIR_KVANTUM}
	install -d ${DIR_SDDM}
	install -d ${DIR_ICONS}
	install -d ${DIR_THEMES}
	install -d "${DIR_ICONS}/DeepinV20White"
	install -d "${DIR_ICONS}/DeepinV20White/cursors"
	install -d "${DIR_ICONS}/DeepinV20Dark"
	install -d "${DIR_ICONS}/DeepinV20Dark/cursors"

	cp --recursive ${PWD}/aurorae/*                         ${DIR_AURORAE}
	cp --recursive ${PWD}/color-schemes/*.colors            ${DIR_SCHEMES}
	cp --recursive ${PWD}/plasma/desktoptheme/DeepinV20*	${DIR_PLASMA}
	cp --recursive ${PWD}/plasma/look-and-feel/*            ${DIR_LOOKFEEL}
	cp --recursive ${PWD}/wallpaper/*                       ${DIR_WALLPAPER}
	cp --recursive ${PWD}/Kvantum/*                         ${DIR_KVANTUM}
	cp --recursive ${PWD}/themes/DeepinV20*                ${DIR_THEMES}
	cp --recursive ${PWD}/sddm/DeepinV20*                  ${DIR_SDDM}
	cp --recursive ${PWD}/icons/DeepinV20White             ${DIR_ICONS}
}