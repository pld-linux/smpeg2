Summary:	SDL2 MPEG Library
Summary(pl.UTF-8):	Biblioteka SDL2 MPEG
Summary(pt_BR.UTF-8):	Biblioteca MPEG SDL2
Summary(ru.UTF-8):	SDL2 MPEG библиотека и проигрыватель
Summary(uk.UTF-8):	SDL2 MPEG бібліотека та програвач
Name:		smpeg2
Version:	2.0.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.libsdl.org/projects/smpeg/release/%{name}-%{version}.tar.gz
# Source0-md5:	0dd8ed3c25e0aa8eb3ac96fdec5c0283
Patch0:		%{name}-optimize.patch
#Patch2:		format-security.patch
URL:		http://icculus.org/smpeg/
BuildRequires:	SDL2-devel >= 2.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	smpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and
SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%description -l pl.UTF-8
SMPEG jest opartym na mpeg_play z UC Berkeley programowym dekoderem
MPEG. SMPLAY jest dekoderem audio stworzonym przez Woo-jae Jung.
Skompletowano prace tych dwóch projektów, aby stworzyć odtwarzacz MPEG
video/audio ogólnego przeznaczenia dla systemu Linux.

%description -l pt_BR.UTF-8
A SMPEG é baseada no software de decodificação MPEG mpeg_play da
Universidade de Berkeley e no SPLAY, um decodificador de áudio mpeg
criado por Woo-jae Jung. Completamos o trabalho inicial de casar estes
dois projetos para criar um reprodutor MPEG de vídeo e áudio de
propósito geral para o sistema operacional Linux.

%description -l ru.UTF-8
SMPEG основывается на программном MPEG декодере mpeg_play,
разработанном в UCB (Университете Беркли) и SPLAY, аудио-декодере,
созданном Woo-jae Jung. Эти два проекта были объединены для создания
MPEG-аудио/видео проигрывателя для Linux.

%description -l uk.UTF-8
SMPEG базується на програмному MPEG декодері mpeg_play, розробленому в
UCB (Університеті Берклі) та SPLAY, аудіо-декодері, який створив
Woo-jae Jung. Ці два проекти були об'єднані для створення
MPEG-аудіо/відео програвача для Linux.

%package libs
Summary:	Shared smpeg2 library
Summary(pl.UTF-8):	Współdzielona biblioteka smpeg2
Group:		Libraries

%description libs
Shared smpeg2 library.

%description libs -l pl.UTF-8
Współdzielona biblioteka smpeg2.

%package devel
Summary:	Smpeg2 header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki smpeg2
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SMPEG2
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ, использующих SMPEG2
Summary(uk.UTF-8):	Файли, необхідні для розробки програм, що використовують SMPEG2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	SDL2-devel >= 2.0.0

%description devel
Header files for smpeg2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki smpeg2.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SMPEG2.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм, що
використовують SMPEG2.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ,
использующих SMPEG2.

%package static
Summary:	Smpeg2 static library
Summary(pl.UTF-8):	Biblioteka statyczna smpeg2
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações SMPEG2
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием SMPEG2
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням SMPEG2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Smpeg2 static library.

%description static -l pl.UTF-8
Biblioteka statyczna smpeg2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações SMPEG2.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ,
использующих SMPEG2.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для розробки програм, що
використовують SMPEG2.

%prep
%setup -q
%patch0 -p1

%{__rm} acinclude/{libtool,lt*}.m4

%build
%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%configure \
%ifarch %{ix86}
	--enable-mmx \
%endif
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.SDL_mixer TODO
%attr(755,root,root) %{_bindir}/plaympeg
%{_mandir}/man1/plaympeg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmpeg2-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmpeg2-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smpeg2-config
%attr(755,root,root) %{_libdir}/libsmpeg2.so
%{_libdir}/libsmpeg2.la
%{_includedir}/smpeg2
%{_aclocaldir}/smpeg2.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmpeg2.a
