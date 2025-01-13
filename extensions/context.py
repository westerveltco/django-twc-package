from __future__ import annotations

from copier_templates_extensions import ContextHook

DJMAIN_MIN_PY = "3.10"


class MinMaxVersion(ContextHook):
    def hook(self, context):
        python_versions = context["python_versions"]
        django_versions = context["django_versions"]
        (
            context["python_min_version"],
            context["python_max_version"],
        ) = self.get_min_max_version(python_versions)
        (
            context["django_min_version"],
            context["django_max_version"],
        ) = self.get_min_max_version(django_versions)
        return context

    def get_min_max_version(self, versions: list[str]) -> tuple[str, str]:
        version_map = {version(v): v for v in versions}
        if not version_map:
            return "", ""
        min_version = min(version_map)
        max_version = max(version_map)
        return version_map[min_version], version_map[max_version]


class NoxfileVersions(ContextHook):
    def hook(self, context):
        python_versions = context["python_versions"].copy()
        django_versions = context["django_versions"].copy()

        test_django_main = context.get("test_django_main", False)
        if test_django_main:
            django_versions.append("main")

        context["nox_python_versions"] = self.get_nox_version_list(
            versions=python_versions, prefix="PY"
        )

        lts_versions = ", ".join(
            [f"DJ{v.replace('.', '')}" for v in django_versions if v.endswith(".2")]
        )
        context["nox_django_versions"] = self.get_nox_version_list(
            versions=django_versions,
            prefix="DJ",
            pre_versions=f"\nDJMAIN_MIN_PY = PY{DJMAIN_MIN_PY.replace('.', '')}"
            if test_django_main
            else None,
            post_versions=f"\nDJ_LTS = [{lts_versions}]",
            default_versions_postfix="LTS",
            latest_index=-2 if test_django_main else -1,
        )

        return context

    def get_nox_version_list(
        self,
        *,
        versions: list[str],
        prefix: str,
        pre_versions: str | None = None,
        post_versions: str | None = None,
        default_versions_postfix: str = "VERSIONS",
        latest_index: int = -1,
    ) -> str:
        variable_map = {}
        for v in versions:
            if "." in v:
                variable_map[f"{prefix}{v.replace('.', '')}"] = v
            else:
                variable_map[f"{prefix}{v.upper()}"] = v

        ret = ""
        ret += "\n".join(f'{k} = "{v}"' for k, v in variable_map.items())

        if pre_versions:
            ret += pre_versions

        ret += f"\n{prefix}_VERSIONS = [{', '.join(variable_map.keys())}]"

        if post_versions:
            ret += post_versions

        ret += f"\n{prefix}_DEFAULT = {prefix}_{default_versions_postfix}[0]"
        ret += f"\n{prefix}_LATEST = {prefix}_VERSIONS[{latest_index}]"

        return ret


def version(ver: str) -> tuple[int, ...]:
    """Convert a string version to a tuple of ints, e.g. "3.10" -> (3, 10)"""
    return tuple(map(int, ver.split(".")))
