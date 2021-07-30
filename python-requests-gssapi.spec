%global sname requests-gssapi
%global s_name requests_gssapi

Name:           python-%{sname}
Version:        1.2.2
Release:        2
Summary:        A GSSAPI/SPNEGO authentication handler for python-requests

License:        ISC
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{sname}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools

%global _description\
Requests is an HTTP library, written in Python, for human beings. This\
library adds optional GSSAPI authentication support and supports\
mutual authentication. It includes a fully backward-compatible shim\
for requests-kerberos.

%description %_description

%package -n python3-%{sname}
Summary:        %summary
Requires:       python3-gssapi
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description

%prep
%autosetup -n %{sname}-%{version} -p1

%build

%py3_build

%install
%py3_install

%check
%{__python3} setup.py nosetests

%files -n python3-%{sname}
%doc README.rst AUTHORS HISTORY.rst
%license LICENSE
%{python3_sitelib}/%{s_name}*


%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.2.2-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git-core

* Wed Jun 23 2021 liufeng <liufeng@kylinos.cn> - 1.2.2-1
- Package init
